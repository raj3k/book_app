from django.test import TestCase
from books.models import Book, Author


class TestBookModel(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            title="Test Book",
            publication_date="2022-01-01",
            isbn="1234567890",
            pages_count="100",
            cover_url="https://www.google.com/",
            pub_language="PL"
        )
        self.assertIsInstance(book, Book)


class TestAuthorModel(TestCase):
    def test_create_author(self):
        author = Author.objects.create(
            first_names="Jan",
            last_name="Nowak"
        )
        self.assertIsInstance(author, Author)