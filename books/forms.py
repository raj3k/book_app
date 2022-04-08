from django import forms
from .models import Author, Book
from django.core.exceptions import ValidationError




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
    
    def clean_pub_language(self):
        return self.cleaned_data['pub_language'].lower()


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"