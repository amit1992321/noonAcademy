from django.db import models
from Books.models import Book
from Student.models import Student
# Create your models here.
class LendBook(models.Model):
	lend_book_from = models.DateField()
	lend_book_till = models.DateField()
	Book = models.ForeignKey(Book, on_delete=models.CASCADE)
	Student = models.ForeignKey(Student, on_delete=models.CASCADE)
	