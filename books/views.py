from django.shortcuts import render
from .models import Book, Author


def index(request):
    books = Book.objects.all()
    return render(request, "books/base.html", {"books": books})


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "books/search_results.html", {"search_text": search_text})