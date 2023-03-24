from django.urls import path

from .views import (Home,
                    PublishBook,
                    RegPublisher,
                    AuthPublisher,
                    logoutPublisher,
                    BookDetail,
                    EditBook,
                    DeleteBook)


urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('book/add', PublishBook.as_view(), name='addBook'),
  path('register', RegPublisher.as_view(), name='register'),
  path('login', AuthPublisher.as_view(), name='login'),
  path('logout', logoutPublisher, name='logout'),
  path('book-detail/<int:pk>', BookDetail.as_view(), name='bookDetail'),
  path('book-edit/<int:pk>', EditBook.as_view(), name='editBook'),
  path('book-delete/<int:pk>', DeleteBook.as_view(), name='deleteBook'),
]