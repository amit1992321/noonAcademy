from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=35)
	course = models.CharField(max_length=20)
	semester = models.CharField(max_length=10);
	email = models.CharField(max_length=10)
	mobile = models.CharField(max_length=10)