from django import forms


class SearchForm(forms.Form):
    q = forms.CharField()


class TestForm(forms.Form):
    some_text = forms.CharField()
    boolean = forms.BooleanField(required=False)
    integer = forms.IntegerField()
    email = forms.EmailField()
