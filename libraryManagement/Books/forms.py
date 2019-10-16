from django import forms
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['ISBN', 'title', 'author', 'Class', 'grade', 'semester']
