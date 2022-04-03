from re import search
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.db.models import Q


@api_view()
def books_api_view(request):
    books = Book.objects.all()
    book_serializer = BookSerializer(books, many=True)
    return Response(book_serializer.data)


@api_view()
def books_search(request):
    search_value = request.GET.get("q", "").split()
    term = search_value[1]
    if term == "intitle":
        books = Book.objects.filter(title__icontains=search_value[0])
    if term == "inauthor":
        books = Book.objects.filter(Q(authors__first_names__icontains=search_value[0]) | Q(authors__last_name__icontains=search_value[0]))
    if term == "inpub_language":
        books = Book.objects.filter(pub_language__icontains=search_value[0])
    book_serializer = BookSerializer(books, many=True)
    return Response(book_serializer.data)

