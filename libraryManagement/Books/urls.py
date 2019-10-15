from django.urls import path

from . import views

urlpatterns = [
    path('insert-book/', views.createBook, name='CreateBook'),
    path('availability/', views.availability, name='Availability'),
    path('lend-book/', views.lendBook, name='LendBook'),
    path('return-book/', views.returnBook, name='ReturnBook'),
]
