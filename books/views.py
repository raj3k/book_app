from django.shortcuts import render, get_object_or_404, redirect
from books.forms import SearchForm, BookForm, AuthorForm
from .models import Book
from django.db.models import Q
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from .utils import get_books_from_google_api


def index(request: WSGIRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, "books/base.html", {"books": books})


def book_add(request: WSGIRequest):
    form_book = BookForm(request.POST or None)
    form_author = AuthorForm(request.POST or None)
    if request.POST and form_book.is_valid():
        form_book.save()
        return redirect("/")
    return render(request, 'books/book_add.html', {"form_book": form_book, "form_author": form_author})

def author_add(request: WSGIRequest):
    form_author = AuthorForm(request.POST or None)
    if request.POST and form_author.is_valid():
        form_author.save()
        return redirect("/book-add")


def book_view(request: WSGIRequest, pk: int):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.POST and form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "books/book.html", {"book": book, "form": form})


def book_search(request: WSGIRequest):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET or None)
    search_results = set()
    if form.is_valid():
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data["search_in"]
        if search_in == "title":
            search_results = Book.objects.filter(title__icontains=search)
        if search_in == "author":
            search_results = Book.objects.filter(Q(authors__first_names__icontains=search) | Q(authors__last_name__icontains=search))
        if search_in == "pub_language":
            search_results = Book.objects.filter(pub_language__icontains=search)
    return render(request, "books/search_results.html", {"search_text": search_text, "search_results": search_results, "form": form})


def get_books(request: WSGIRequest):
    if 'search' in request.GET:
        search_value = request.GET.get("search", "")
        get_books_from_google_api(query_arg=search_value)
    all_books = Book.objects.all()
    return render(request, "books/base.html", {"books": all_books})