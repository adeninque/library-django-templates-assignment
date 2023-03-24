from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField(blank=True)
  cover = models.ImageField(upload_to='book_covers/%Y/%m/%d')
  created = models.DateTimeField(auto_now_add=True)
  author = models.ManyToManyField('Author', symmetrical=True)
  publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

  def __str__(self): return self.title
  
class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  photo = models.ImageField(upload_to='author_profile_photos/%Y/%m/%d', default='defs/default-avatar.jpg')
  
  def __str__(self): return self.name

class Publisher(AbstractUser, PermissionsMixin):
  address = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='publisher_profile_photos/%Y/%M/', default='defs/default-avatar.jpg')
  
  def __str__(self): return self.username