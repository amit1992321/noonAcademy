from django.db import models
from Books.models import Book
from LendBook.models import LendBook
from Student.models import Student
# Create your models here.


class ReturnBook(models.Model):
    LendBook = models.ForeignKey(LendBook, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    return_date = models.DateField()
    Fine = models.IntegerField()
