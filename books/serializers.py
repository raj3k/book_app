from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.Serializer):
    first_names = serializers.CharField()
    last_name = serializers.CharField()


class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    publication_date = serializers.CharField()
    isbn = serializers.CharField()
    pages_count = serializers.IntegerField()
    cover_url = serializers.URLField()
    pub_language = serializers.CharField()
    authors = AuthorSerializer(many=True, read_only=True)

