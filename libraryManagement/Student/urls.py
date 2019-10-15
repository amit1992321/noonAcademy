from django.urls import path

from . import views

urlpatterns = [
    path('registration-student/', views.registrationStudent, name='RegStudent'),
]
