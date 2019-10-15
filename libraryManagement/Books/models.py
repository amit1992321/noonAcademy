from django.db import models

# Create your models here.
class Book(models.Model):
	ISBN = models.CharField(max_length=10)
	title = models.CharField(max_length=250)
	Class = models.CharField(max_length=20)
	grade = models.CharField(max_length=20)
	semester = models.CharField(max_length=10)
