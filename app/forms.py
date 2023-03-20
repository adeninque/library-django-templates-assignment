from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import (Book,
                     Author,
                     Publisher)

class DefAttrs:
  def get_def_input_attrs(self, attrs=None):
    def_attrs = {'class': 'form__input'}
    if attrs:
      def_attrs.update(attrs)
    return def_attrs

class TextInput(DefAttrs,
                forms.TextInput):
  def __init__(self, attrs=None):
    super().__init__(self.get_def_input_attrs(attrs))
    
    
class Textarea(DefAttrs,
               forms.Textarea):
  def __init__(self, attrs=None):
    super().__init__(self.get_def_input_attrs(attrs))


class FileInput(forms.FileInput):
  def __init__(self, attrs=None):
      def_attrs = {'class': 'form__file'}
      if attrs:
        def_attrs.update(attrs)
      super().__init__(def_attrs)    
    
    
class SelectMultiple(DefAttrs,
                     forms.SelectMultiple):
  def __init__(self, attrs=None):
    super().__init__(self.get_def_input_attrs(attrs))
    
    
class EmailInput(DefAttrs,
                forms.EmailInput):
  def __init__(self, attrs=None):
    super().__init__(self.get_def_input_attrs(attrs))
    
    
class PasswordInput(DefAttrs,
                forms.PasswordInput):
  def __init__(self, attrs=None):
    super().__init__(self.get_def_input_attrs(attrs))
    

    
class AddBook(forms.ModelForm):
  class Meta:
    model = Book
    fields = ('title', 'body', 'cover', 'author', )
    widgets = {
      'title': TextInput(),
      'body': Textarea(),
      'cover': FileInput(),
      'author': SelectMultiple(),
    }
  
  
class CreateUserForm(UserCreationForm):
  class Meta:
    model = Publisher
    fields = ('username', 'email', 'password1', 'password2')
    widgets = {
      'username': TextInput(),
      'email': EmailInput(),
      'password1': PasswordInput(),
      'password2': PasswordInput(),
    }
  
  
class AuthUserForm(AuthenticationForm):
  class Meta:
    model = Publisher
    fields = ('username', 'password')
    widgets = {
      'username': TextInput(),
      'password': PasswordInput(),
    }