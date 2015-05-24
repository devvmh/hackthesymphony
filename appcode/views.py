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

def suggestions(request, pk):
  session = Session.objects.get(pk=pk)
  session_answer_list = SessionAnswer.objects.filter(session=session)
  return render(request, 'suggestions.html', {
    session_answer_list: session_answer_list,
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
