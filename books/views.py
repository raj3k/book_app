from django.shortcuts import render


def index(request):
    return render(request, "books/base.html")


def book_search(request):
    pass