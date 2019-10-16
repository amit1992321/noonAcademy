# Generated by Django 2.2.6 on 2019-10-16 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13)),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=50)),
                ('Class', models.CharField(choices=[('Computer Science and Engineering', 'CSE'), ('Electronics and Communication Engineering', 'ECE'), ('Electrical Engineering', 'EE'), ('Mechanical Engineering', 'ME'), ('Civil Engineering', 'CIVIL E'), ('Petroleum Engineering', 'PE'), ('Chemical Engineering', 'CE'), ('Aerospace Engineering', 'AE'), ('Industrial Engineering', 'IE'), ('Aeronautical Engineering', 'AERO E'), ('Medical', 'MEDICAL'), ('Finance', 'FFNANCE'), ('Computer Application', 'Comp App')], default='Computer Science and Engineering', max_length=50, null=True)),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='A', max_length=5, null=True)),
                ('semester', models.CharField(choices=[('First', 'I'), ('Second', 'II'), ('Third', 'III'), ('Fourth', 'IV'), ('Five', 'V'), ('Six', 'VI'), ('Sevan', 'VII'), ('Eight', 'VIII')], default='First', max_length=15, null=True)),
            ],
        ),
    ]
