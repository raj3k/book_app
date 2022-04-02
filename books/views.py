from django.shortcuts import render, get_object_or_404
from books.forms import SearchForm, BookForm
from .models import Book, Author
from django.db.models import Q


def index(request):
    books = Book.objects.all()
    return render(request, "books/base.html", {"books": books})


def book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(instance=book)
    return render(request, "books/book.html", {"book": book, "form": form})


def book_search(request):
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