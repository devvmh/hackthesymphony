from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from rest_framework import routers

from .views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'session-answers', SessionAnswerViewSet)

urlpatterns = patterns('appcode.views',
  url(r'^$', 'index', name='index'),
  url(r'what-is-this/$', 'what_is_this', name='index'),
  url(r'suggestions/(?P<pk>\d+)/$', 'suggestions', name='suggestions'),
  url(r'^api/', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  url(r'^scores/$', 'scores_edit_table', name='scores-edit-table'),
  url(r'^scores/submit/$', 'scores_edit_table_submit', name='scores-edit-table-submit'),
)
