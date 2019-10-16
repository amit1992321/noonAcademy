
from django import forms
from . import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['UID', 'name', 'course', 'semester', 'email', 'mobile']
