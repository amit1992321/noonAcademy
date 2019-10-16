from django.shortcuts import render
from .forms import LendBookForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from Books.models import Book
# Create your views here.


def lendBook(request):
    error = ''
    BookObj = Book.objects.all()
    if request.method == "POST":
        lend_book = LendBookForm(request.POST)
        context = {
            'BookObj': BookObj,
            'lend_book': lend_book,
            'errors': error
        }
        if lend_book.is_valid():
            lend_book.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        lend_book = LendBookForm()
        context = {
            'BookObj': BookObj,
            'lend_book': lend_book,
            'errors': error
        }
    return render(request, "lend-book.html", context)


def availability(request):
    obj = Book.objects.all()
    return render(request, "availability.html", {'obj': obj})
