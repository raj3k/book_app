from django.test import TestCase
from books.models import Book, Author


class TestBookModel(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_names="Jan",
            last_name="Nowak"
        )
        self.book = Book.objects.create(
            title="Test Book",
            publication_date="2022-01-01",
            isbn="1234567890",
            pages_count=100,
            cover_url="https://www.google.com",
            pub_language="Pl",
        )
        self.book.authors.add(self.author)
        

    def test_create_book(self):
        self.assertIsInstance(self.book, Book)

    def test_str_representation(self):
        self.assertEquals(str(self.book), "Test Book")


class TestAuthorModel(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_names="Jan",
            last_name="Nowak"
        )

    def test_create_author(self):
        self.assertIsInstance(self.author, Author)


class TestBookAuthor(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_names="Jan",
            last_name="Nowak"
        )
        self.book = Book.objects.create(
            title="Test Book",
            publication_date="2022-01-01",
            isbn="1234567890",
            pages_count=100,
            cover_url="https://www.google.com",
            pub_language="Pl",
        )
        self.book.authors.add(self.author)

    def test_bookauthor_relation(self):
        self.assertEqual(self.book.authors.get(pk=self.author.pk), self.author)