from django.urls import path

from . import views

urlpatterns = [
    path('insert-book/', views.createBook, name='CreateBook'),
]