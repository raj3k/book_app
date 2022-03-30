from django.shortcuts import render


def index(request):
    return render(request, "books/base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "books/search_results.html", {"search_text": search_text})