from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('code.views',
  url(r'^$', 'index'),
  url(r'question/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='question-detail'),
)
