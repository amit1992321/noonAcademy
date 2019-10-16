from django.urls import path

from . import views

urlpatterns = [
    path('return-book/', views.returnBook, name='ReturnBook'),
]
