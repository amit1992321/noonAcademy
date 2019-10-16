from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=35)
    UID = models.CharField(max_length=20)
    COURSE = (
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('B.TECH', 'B.Tech'),
        ('BSC', 'bsc'),
        ('MBBS', 'Mbbs'),
        ('B.COM', 'B.Com'),
        ('M.COM', 'M.Com'),
        ('MSC', 'Msc'),
        ('PHD', 'Phd'),
        ('M.TECH', 'M.Tech'),
        ('MS', 'Ms'),
    )
    course = models.CharField(max_length=25, null=True,
                              default=COURSE[0][0], choices=COURSE)
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
    semester = models.CharField(max_length=20, null=True,
                                default=SEMESTER[0][0], choices=SEMESTER)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField()
