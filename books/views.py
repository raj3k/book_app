from django.shortcuts import render, get_object_or_404
from books.forms import SearchForm, BookForm
from .models import Book, Author
from django.db.models import Q
import requests


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


def get_books(request):
    if 'search' in request.GET:
        search_value = request.GET["search"]
        url = f"https://www.googleapis.com/books/v1/volumes?q={search_value}"
        response = requests.get(url)
        data = response.json()
        books = data["items"]

        for book in books:
            thumbnail = ""
            pagecount = None
            if "imageLinks" in book["volumeInfo"].keys():
                thumbnail = book["volumeInfo"]["imageLinks"]["thumbnail"]

            if "pageCount" in book["volumeInfo"].keys():
                pagecount = book["volumeInfo"]["pageCount"]

            book_data = Book(
                title = book["volumeInfo"]["title"],
                publication_date = book["volumeInfo"]["publishedDate"],
                isbn = book["volumeInfo"]["industryIdentifiers"][0]["identifier"],
                pages_count = pagecount,
                cover_url = thumbnail,
                pub_language = book["volumeInfo"]["language"]
            )

            book_data.save()

            for author in book["volumeInfo"]["authors"]:
                book_data.authors.create(first_names=" ".join(author.split()[:-1]), last_name=author.split()[-1])
                # TODO: sprawdzanie czy dane imie nazwisko juz istnieje zeby nie duplikowac rekordow w bazie

    all_books = Book.objects.all()
    return render(request, "books/base.html", {"books": all_books})