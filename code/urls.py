from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('code.views',
  url(r'^$', 'index'),
#  url(r'^example/$', ExampleListView.as_view()), name='example-list'),
#  url(r'^example/(?P<pk>\d+)/$', ExampleDetailView.as_view()), name='example-detail'),
)
