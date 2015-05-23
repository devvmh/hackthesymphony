from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('appcode.views',
  url(r'^$', 'index'),
  url(r'^raw/questions/$', 'raw_question_list', name='raw-question-list'),
  url(r'^raw/questions/(?P<pk>\d+)/$', 'raw_question_detail', name='raw-question-detail'),
  url(r'^raw/answers/$', 'raw_answer_list', name='raw-answer-list'),
  url(r'^raw/answers/(?P<pk>\d+)/$', 'raw_answer_detail', name='raw-answer-detail'),
  url(r'questions/(?P<pk>\d+)/$', 'question_detail', name='question-detail'),
)
