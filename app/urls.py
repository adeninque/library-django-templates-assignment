from django.urls import path

from .views import (Home,
                    PublishBook,
                    RegPublisher,
                    AuthPublisher,
                    logoutPublisher)


urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('book/add', PublishBook.as_view(), name='addBook'),
  path('register', RegPublisher.as_view(), name='register'),
  path('login', AuthPublisher.as_view(), name='login'),
  path('logout', logoutPublisher, name='logout')
]