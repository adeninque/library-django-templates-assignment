from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField(blank=True)
  cover = models.ImageField()
  created = models.DateTimeField(auto_now_add=True)
  author = models.ManyToManyField('Author', symmetrical=True)
  publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)

class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

class Publisher(AbstractUser, PermissionsMixin):
  address = models.CharField(max_length=255)