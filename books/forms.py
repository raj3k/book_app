from django import forms
from .models import Author, Book
from django.core.exceptions import ValidationError


def validate_lower(value):
        if value.lower() != value:
            raise ValidationError(f"{value} is not lowercase!")


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
        exclude = '__all__'
    pub_language = forms.CharField(max_length=2, validators=[validate_lower])


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"