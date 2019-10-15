from django.db import models

# Create your models here.


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    CLASS = (
        ('Computer Science and Engineering', 'CSE'),
        ('Electronics and Communication Engineering', 'ECE'),
        ('Electrical Engineering', 'EE'),
        ('Mechanical Engineering', 'ME'),
        ('Civil Engineering', 'CIVIL E'),
        ('Petroleum Engineering', 'PE'),
        ('Chemical Engineering', 'CE'),
        ('Aerospace Engineering', 'AE'),
        ('Industrial Engineering', 'IE'),
        ('Aeronautical Engineering', 'AERO E'),
        ('Medical', 'MEDICAL'),
        ('Finance', 'FFNANCE'),
        ('Computer Application', 'Comp App')
    )
    Class = models.CharField(max_length=50,
                             null=True,
                             default=CLASS[0][0],
                             choices=CLASS)
    GRADE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    grade = models.CharField(max_length=5, null=True,
                             default=GRADE[0][0], choices=GRADE)
    SEMESTER = (
        ('First', 'I'),
        ('Second', 'II'),
        ('Third', 'III'),
        ('Fourth', 'IV'),
        ('Five', 'V'),
        ('Six', 'VI'),
        ('Sevan', 'VII'),
        ('Eight', 'VIII'),

    )
    semester = models.CharField(max_length=15, null=True,
                                default=SEMESTER[0][0], choices=SEMESTER)
