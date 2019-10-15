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


def availability(request):
    return render(request, "availability.html", {})


def lendBook(request):
    return render(request, "lend-book.html", {})


def returnBook(request):
    return render(request, "return-book.html", {})
