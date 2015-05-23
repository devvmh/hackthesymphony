from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseBadRequest, Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.views.generic import DetailView, UpdateView, ListView

from .models import *

def index(request):
  return render(request, 'index.html', {})

def question_detail(request, pk):
  question = Question.objects.get(pk=pk)
  answer_list = Answer.objects.filter(old_question=question)
  return render(request, 'question_detail.html', {
    'question': question,
    'answer_list': answer_list,
  })

def raw_question_list(request):
  questions = Question.objects.all()
  json_dump = serializers.serialize("json", questions)
  return HttpResponse(json_dump, content_type="application/json")

def raw_question_detail(request, pk):
  question = get_object_or_404(Question, pk=pk)
  json_dump = serializers.serialize("json", [question])
  json_dump = json_dump[1:-1] #strip array bits off
  return HttpResponse(json_dump, content_type="application/json")

def raw_answer_list(request):
  json_dump = serializers.serialize("json", Answer.objects.all())
  return HttpResponse(json_dump, content_type="application/json")

def raw_answer_detail(request, pk):
  answer = get_object_or_404(Answer, pk=pk)
  json_dump = serializers.serialize("json", [answer])
  json_dump = json_dump[1:-1] #strip array bits off
  return HttpResponse(json_dump, content_type="application/json")
