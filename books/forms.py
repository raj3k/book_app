from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(min_length=2)
    search_in = forms.ChoiceField(required=False, choices=(
        ("title", "Title"),
        ("author", "Author"),
        ("pub_language", "Language")
    ))