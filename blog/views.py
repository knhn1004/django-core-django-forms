from django.shortcuts import render
from .forms import SearchForm

def home(req):
    form = SearchForm()
    return render(req, 'form.html', {'form': form})