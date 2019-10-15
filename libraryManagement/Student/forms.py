
from django import forms
import datetime
from . import models
from django.forms import formset_factory


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['name', 'course', 'semester', 'email', 'mobile']
