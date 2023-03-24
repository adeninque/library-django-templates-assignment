from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.urls import reverse_lazy

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField(blank=True)
  cover = models.ImageField(upload_to='book_covers/%Y/%m/%d')
  created = models.DateTimeField(auto_now_add=True)
  author = models.ManyToManyField('Author', symmetrical=True)
  publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

  def __str__(self): return self.title
  
  def get_url_to(self, to: str): return reverse_lazy(to, kwargs={'pk': self.pk})
  
  def get_absolute_url(self): return self.get_url_to('bookDetail')
  def get_edit_url(self): return self.get_url_to('editBook')
  def get_delete_url(self): return self.get_url_to('deleteBook')
  
class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  photo = models.ImageField(upload_to='author_profile_photos/%Y/%m/%d', default='defs/default-avatar.jpg')
  
  def __str__(self): return self.name

class Publisher(AbstractUser, PermissionsMixin):
  address = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='publisher_profile_photos/%Y/%M/', default='defs/default-avatar.jpg')
  
  def __str__(self): return self.username