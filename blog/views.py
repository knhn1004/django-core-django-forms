from django.http import request
from django.shortcuts import render
from .forms import SearchForm, TestForm


def home(req):
    form = TestForm(req.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        print(form.cleaned_data.get('some_text'))
    # if req.method == 'POST':
    #    pass
    # elif req.method == 'GET':
    #    pass
    return render(req, 'form.html', {'form': form})
