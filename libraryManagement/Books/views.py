from django.shortcuts import render


def createBook(request):
    return render(request, "createBook.html", {})
