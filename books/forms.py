from django import forms
from .models import Author, Book


class SearchForm(forms.Form):
    search = forms.CharField(min_length=2)
    search_in = forms.ChoiceField(required=False, choices=(
        ("title", "Title"),
        ("author", "Author"),
        ("pub_language", "Language")
    ))

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"