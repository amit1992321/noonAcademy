from django.urls import path

from . import views

urlpatterns = [
    path('availability/', views.availability, name='Availability'),
    path('lend-book/', views.lendBook, name='LendBook'),
]
