from django.shortcuts import render
from .forms import BookForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def createBook(request):
    error = ''
    if request.method == "POST":
        book = BookForm(request.POST)
        context = {
            'book': book,
            'errors': error
        }
        if book.is_valid():
            book.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        book = BookForm()
        context = {
            'book': book,
            'errors': error
        }
    return render(request, "createBook.html", context)
