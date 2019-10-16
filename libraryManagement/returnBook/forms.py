from django import forms
from . import models


class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = models.ReturnBook
        fields = ['LendBook', 'Book', 'Student', 'return_date', 'Fine']
