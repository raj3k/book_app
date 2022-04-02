from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, help_text="The title of the book.")
    publication_date = models.CharField(max_length=20, verbose_name="Publication date of the book")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book")
    pages_count = models.IntegerField(verbose_name="Number of pages in the book", null=True, blank=True)
    cover_url = models.URLField(verbose_name="URL to book cover")
    pub_language = models.CharField(max_length=2, verbose_name="Language of the book publication")
    authors = models.ManyToManyField('Author', through="BookAuthor")

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    first_names = models.CharField(max_length=50, verbose_name="The contributor first name or names")
    last_name = models.CharField(max_length=50, verbose_name="The contributor last name")

    def __str__(self) -> str:
        return self.first_names + " " + self.last_name


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

