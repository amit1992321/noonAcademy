from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def registrationStudent(request):
    error = ''
    if request.method == "POST":

        student = StudentForm(request.POST)
        context = {
            'student': student,
            'errors': error
        }
        if student.is_valid():
            student.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        student = StudentForm()
        context = {
            'student': student,
            'errors': error
        }

    return render(request, "registration-student.html", context)
