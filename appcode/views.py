from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseBadRequest, Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.views.generic import DetailView, UpdateView, ListView

from rest_framework import viewsets

from .models import *
from .serializers import *

def index(request):
  return render(request, 'index.html', {
    'ip_address': '192.168.1.99',
    'body_classes': 'index main-quiz',
  })

def what_is_this(request):
  return render(request, 'what-is-this.html', {
    'body_classes': 'what-is-this',
  })

def suggestions(request, pk):
  session = get_object_or_404(Session, pk=pk)
  session_answer_list = SessionAnswer.objects.filter(session=session.pk)
  knowledge = get_answer_concert_array()
  concerts = [{'pk': x+1, 'score': 0} for x in range(0,14)]
  for session_answer in session_answer_list:
    ans = session_answer.answer.pk
    print 'ans', ans
    for i in range(0,14):
      print 'i', i
      try:
        concerts[i]['score'] += knowledge[ans][i+1]
      except:
        print 'fixme TODO: that answer or concert doesn\'t exist in array'
  concerts = sorted(concerts, key=lambda x: -x['score'])
  concert_list = [Concert.objects.get(pk=x['pk']) for x in concerts[:3]]

  return render(request, 'suggestions.html', {
    'concert_list': concert_list,
    'body_classes': 'suggestions',
  })

class QuestionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class SessionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionAnswerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = SessionAnswer.objects.all()
    serializer_class = SessionAnswerSerializer

@login_required
def concert_scores_edit_table(request):
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
        score_list[aindex][cindex] = ConcertAnswerScore.objects.get(answer=answer, concert=concert).score
      except:
        #if the score doesn't exist, make it exist and equal to 0
        mapping = ConcertAnswerScore(answer=answer, concert=concert, score=0)
        mapping.save()
        score_list[aindex][cindex] = 0

  return render(request, 'concert_scores_edit_table.html', {
    'concert_list': concert_list,
    'answer_list': answer_list,
    'score_list': score_list,
    'body_classes': 'suggestions quiz-complete',
  })

def get_answer_concert_array():
  #this is indexed by answer and then by concert
  rows = []
  rows.append([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
  rows.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
  rows.append([2,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
  rows.append([3,0,0,0,0,0,0,0,0,0,0,0,0,1,0])
  rows.append([4,1,0,1,0,0,1,0,0,0,1,0,0,0,0])
  rows.append([5,0,0,0,0,0,0,0,1,1,0,1,0,1,0])
  rows.append([6,0,0,0,0,0,0,0,0,-1,1,-1,0,0,-1])
  rows.append([7,1,1,0,1,0,1,0,1,0,1,0,0,0,1])
  rows.append([8,0,1,1,1,0,1,0,0,0,1,0,0,0,0])
  rows.append([9,1,-1,0,0,1,0,2,2,2,1,2,0,1,2])
  rows.append([10,1,2,0,1,1,1,0,1,0,1,0,0,0,0])
  rows.append([11,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
  rows.append([12,0,0,0,0,0,0,0,0,0,0,0,4,1,0])
  rows.append([13,0,0,2,0,0,0,0,0,0,0,0,4,1,0])
  rows.append([14,0,1,1,0,0,1,0,1,0,1,1,0,1,0])
  rows.append([15,1,1,1,1,0,1,1,1,0,2,1,0,1,0])
  rows.append([16,0,0,0,0,0,0,0,1,2,0,2,0,1,1])
  rows.append([17,0,1,0,1,0,1,0,0,-1,0,-1,1,0,0])
  rows.append([18,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
  rows.append([19,1,0,0,0,1,0,1,1,1,0,1,0,0,1])
  rows.append([20,0,0,0,0,0,0,0,1,2,0,2,0,1,1])
  rows.append([21,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
  rows.append([22,0,0,0,0,0,0,3,0,0,0,0,0,0,0])
  rows.append([23,0,3,0,0,0,0,0,0,0,0,0,0,0,0])
  rows.append([24,2,0,0,0,3,0,0,0,0,0,0,0,0,0])
  rows.append([25,0,0,0,3,0,0,0,0,0,0,0,0,0,0])
  rows.append([26,0,0,0,0,0,0,0,0,3,0,3,0,0,0])
  rows.append([27,0,0,2,0,0,1,0,0,0,0,0,2,1,0])
  rows.append([28,1,1,1,2,1,2,1,0,0,2,0,0,1,0])
  rows.append([29,0,0,0,0,1,0,1,0,2,0,2,0,1,1])
  return rows 
