from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, ListView
from django.contrib import messages

from .models import *

def index(request):
  return render(request, 'index.html', {})

class QuestionDetailView(DetailView):
  model = Question
  context_object_name = 'question'

def question_detail(request, pk):
  question = Question.objects.get(pk=pk)
  answer_list = Answer.objects.get(old_question=question)
  return render(request, 'question_detail.html', {
    'question': question,
    'answer_list': answer_list,
  })
