from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .utils import DataMixin
from .forms import (AddBook,
                    CreateUserForm,
                    AuthUserForm)

# Create your views here.
class Home(DataMixin, TemplateView):
  template_name = 'app/home.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update(self.get_extra_context())
    return context
  

class PublishBook(DataMixin, LoginRequiredMixin ,CreateView):
  form_class = AddBook
  template_name = 'app/form.html'
  success_url = reverse_lazy('home')
  login_url = reverse_lazy('login')
  
  def form_valid(self, form: BaseModelForm) -> HttpResponse:
    form.instance.publisher = self.request.user
    return super().form_valid(form)
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update(self.get_extra_context(
      title = 'Add Book'
    ))
    return context


class RegPublisher(DataMixin, CreateView):
  form_class = CreateUserForm
  template_name = 'app/reg-auth.html'
  success_url = reverse_lazy('home') 
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update(self.get_extra_context(
      title = "Register",
      reg = True
    ))
    return context
  
  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect(self.success_url)


class AuthPublisher(DataMixin, LoginView):
  form_class = AuthUserForm
  template_name = 'app/reg-auth.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update(self.get_extra_context(
      title = "Login",
      reg = False
    ))
    return context

def logoutPublisher(request: HttpRequest):
  logout(request)
  return redirect('/')