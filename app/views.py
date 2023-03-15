from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView

from .forms import (AddBook)

# Create your views here.
class Home(TemplateView):
  template_name = 'app/home.html'
  

class PublishBook(CreateView):
  form_class = AddBook
  success_url = '/'