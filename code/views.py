from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, ListView
from django.contrib import messages

from .models import *

def index(request):
  return render(request, 'index.html', {})

#class ExampleListView(ListView):
#  model = Example
#  context_object_name = 'example_list'
#  #paginate_by = 10
#  #template_name = 'special.html'
#
#class ExampleDetailView(DetailView):
#  model = Example
#  context_object_name = 'example'
