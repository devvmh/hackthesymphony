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
  })

def what_is_this(request):
  return render(request, 'what-is-this.html', {
  })

def suggestions(request, pk):
  session = Session.objects.get(pk=pk)
  session_answer_list = SessionAnswer.objects.filter(session=session.pk)
  knowledge = get_answer_concert_array()
  concerts = [{'pk': x+1, 'score': 0} for x in range(0,14)]
  for session_answer in session_answer_list:
    ans = session_answer.answer.pk
    for i in range(0,14):
      concerts[i]['score'] += knowledge[ans][i+1]
  concerts = sorted(concerts, key=lambda x: -x['score'])
  concert_list = [Concert.objects.get(pk=x['pk']) for x in concerts[:3]]

  return render(request, 'suggestions.html', {
    'concert_list': concert_list,
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
