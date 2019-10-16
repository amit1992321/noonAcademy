from django.shortcuts import render
# from LendBook.models import LendBook
from Books.models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse
from Student.models import Student
from .forms import ReturnBookForm
# Create your views here.


def returnBook(request):
    # obj_lend = LendBook.objects.all()
    obj_book = Book.objects.last()
    obj_student = Student.objects.last()
    error = ''
    if request.method == "POST":
        return_book = ReturnBookForm(request.POST or None)
        context = {
            'return_book': return_book,
            'errors': error
        }
        if return_book.is_valid():
            data = ReturnBookForm.cleaned_data.get(return_book.ISBN)
            obj_book = Book.objects.filter(ISBN=data)
            data1 = ReturnBookForm.cleaned_data.get(return_book.UID)
            obj_student = Student.objects.filter(UID=data1)
            # return_book.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        return_book = ReturnBookForm()
        context = {
            'return_book': return_book,
            'errors': error
        }
    return render(request, "return-book.html", {
        'obj_book': obj_book,
        'obj_student': obj_student
    },

        context)
