from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from rest_framework import routers

from .views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'session-answers', SessionAnswerViewSet)

urlpatterns = patterns('appcode.views',
  url(r'^$', 'index', name='index'),

  url(r'^login$', 'django.contrib.auth.views.login'),
  url(r'^logout$', 'django.contrib.auth.views.logout'),
  url(r'^admin/', include(admin.site.urls)),

  url(r'^api/', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#  url(r'^js-restAPI/?$', restApi.as_view(), {'router': router, 'url_prefix':'/api',}, name='rest-api'),
)
