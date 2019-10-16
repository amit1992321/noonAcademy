from django.shortcuts import render
# from LendBook.models import LendBook
# from Books.models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse
# from Student.models import Student
from .forms import ReturnBookForm
# Create your views here.


def returnBook(request):
    # obj_lend = LendBook.objects.all()
    # obj_book = Book.objects.all()
    # obj_student = Student.objects.all()
    error = ''
    if request.method == "POST":

        return_book = ReturnBookForm(request.POST)
        context = {
            'return_book': return_book,
            'errors': error
        }
        if return_book.is_valid():
            return_book.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        return_book = ReturnBookForm()
        context = {
            'return_book': return_book,
            'errors': error
        }
    return render(request, "return-book.html",
                  context)
