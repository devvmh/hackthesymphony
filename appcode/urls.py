from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'questions', QuestionSerializer)
router.register(r'answers', AnswerSerializer)
router.register(r'sessions', SessionSerializer)
router.register(r'session-answers', SessionAnswersSerializer)

urlpatterns = patterns('appcode.views',
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#  url(r'questions/(?P<pk>\d+)/$', 'question_detail', name='question-detail'),

)
