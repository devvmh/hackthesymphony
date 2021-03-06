from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.serializers import serialize
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseBadRequest, Http404, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.views.generic import DetailView, UpdateView, ListView

import re, random, json

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from .models import *
from .serializers import *

def index(request):
  questions_json = serialize("json", Question.objects.all())
  answers_json = serialize("json", Answer.objects.all())

  return render(request, 'index.html', {
    'ip_address': request.META['REMOTE_ADDR'],
    'body_classes': 'index main-quiz',
    'questions_json': questions_json,
    'answers_json': answers_json,
  })

def what_is_this(request):
  return render(request, 'what-is-this.html', {
    'body_classes': 'what-is-this',
  })

def date_passed(concert):
  from dateutil import parser
  from datetime import date
  today_date = date.today()

  #parse dat
  datestr = concert.date.split("\n")[-1]
  concert_date = None
  try:
    concert_date = parser.parse(datestr).date()
  except ValueError:
    return false #just include this concert just in case

  #has the concert already passed?
  return (concert_date < today_date)

def suggestions(request, pk):
  #grab the session and its answers
  session = get_object_or_404(Session, pk=pk)
  session_answer_list = SessionAnswer.objects.filter(session=session.pk)

  #set up a dict of the scores for each concert
  concert_scores = {}
  for concert in Concert.objects.in_the_future():
    concert_scores[str(concert.pk)] = {'pk': concert.pk, 'score': 0}

  #for each answer the user provided, add scores for each relevant concert
  for session_answer in session_answer_list:
    for concert in Concert.objects.in_the_future():
      concert_scores[str(concert.pk)]['score'] += get_score(session_answer.answer, concert)

  #sort the concerts by score in descending order; grab the top 3
  #random.shuffle means that ties will be randomized
  concert_scores = [concert_scores[x] for x in concert_scores]
  random.shuffle(concert_scores)
  concert_scores = sorted(concert_scores, key=lambda x: -x['score'])
  concert_list = [Concert.objects.get(pk=x['pk']) for x in concert_scores[:3]]

  return render(request, 'suggestions.html', {
    'concert_list': concert_list,
    'body_classes': 'suggestions quiz-complete',
  })


class SessionViewSetPermission(permissions.BasePermission):
  """You can create (POST) a new session for free with a csrf_token; then you 
     need that csrf_token to be able to update (PUT) it"""
  def has_object_permission(self, request, view, obj):
    if request.method == 'POST':
      return True
    elif request.method == 'PUT' and request.META.get('HTTP_X_SESSION_TOKEN'):
      return obj.session_token == request.META['HTTP_X_SESSION_TOKEN']
    else:
      return request.user.is_staff #todo use DjangoModelPermissions

class SessionAnswerViewSetPermission(permissions.BasePermission):
  """You can create a new session answer only with a valid session's 
     csrf_token"""
  def has_object_permission(self, request, view, obj):
    if request.method == 'POST' and request.META.get('HTTP_X_SESSION_TOKEN'):
      session = obj.session
      
      return session.session_token == request.META['HTTP_X_SESSION_TOKEN']
    else:
      return request.user.is_staff #todo use DjangoModelPermissions

class QuestionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class SessionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    permission_classes = (SessionViewSetPermission, )
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionAnswerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    permission_classes = (SessionAnswerViewSetPermission, )
    queryset = SessionAnswer.objects.all()
    serializer_class = SessionAnswerSerializer

@permission_required('change_concertanswerscore', login_url='/admin/login/')
def scores_edit_table(request):
  concert_list = Concert.objects.all()
  answer_list = Answer.objects.all()

  #generate an array filled with scores and blank entries
  score_list = {}
  for answer in answer_list:
    #this is the "rows": each answer maps to a bunch of concerts
    aindex = str(answer.pk)
    #create a new python dictionary to store the concert scores for this answer
    score_list[aindex] = {}
    for concert in concert_list:
      cindex = str(concert.pk)
      try:
        #if the score exists, grab it
        mapping = ConcertAnswerScore.objects.get(answer=answer, concert=concert)
      except:
        #if the score doesn't exist, make it exist and equal to 0
        mapping = ConcertAnswerScore(answer=answer, concert=concert, score=0)
        mapping.save()
      score_list[aindex][cindex] = mapping

  return render(request, 'scores_edit_table.html', {
    'concert_list': concert_list,
    'answer_list': answer_list,
    'score_list': score_list,
    'body_classes': 'scores scores-edit scores-edit-table',
  })

@login_required(login_url='/admin/login/')
def scores_edit_table_submit(request):
  if not request.POST:
    return HttpResponseNotAllowed
  
  #check each key in the post, and if it's an integer then update the score
  #the keys must be in the form mapping-<number> to work
  for key in request.POST:
    #get pk
    r = re.compile('mapping-(\d*)')
    if r.match(key) is None:
      continue
    mapping_pk = int(key.replace('mapping-', ''))

    #make sure that pk exists and the input value is a number
    try:
      mapping = ConcertAnswerScore.objects.get(pk=mapping_pk)
      oldscore = mapping.score
      mapping.score = int(request.POST[key])
    except:
      messages.error(request, 'error on ' + request.POST[key])
      continue

    #update the score
    if oldscore != mapping.score:
      mapping.save()
      messages.success(request, 'Updated score for mapping #' + unicode(mapping.pk) + ', which deals with Answer "' + unicode(mapping.answer.answer) + '" and Concert "' + unicode(mapping.concert.title) + '".')

  return redirect('scores-edit-table')

def get_score(answer, concert):
  try:
    mapping = ConcertAnswerScore.objects.get(answer=answer, concert=concert)
    return mapping.score
  except:
    print "Problem retrieving score mapping for concert=" + str(concert.pk) + " and answer=" + str(answer.pk) + "; returning 0."
    return 0
