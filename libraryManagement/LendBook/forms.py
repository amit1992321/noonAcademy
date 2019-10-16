from django import forms
from . import models


class LendBookForm(forms.ModelForm):
    class Meta:
        model = models.LendBook
        fields = ['lend_book_from', 'lend_book_till', 'Book', 'Student']
