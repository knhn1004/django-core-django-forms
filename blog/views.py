from django.http import request
from django.shortcuts import render
from django.utils import timezone

from .forms import SearchForm, TestForm, PostModelForm


def home(req):
    # if req.method == 'POST':
    #    form = TestForm(data=req.POST)
    #    # print(req.POST)
    #    # print(req.POST.get('username'))
    #    if form.is_valid():
    #        print(form.cleaned_data)
    #        print(form.cleaned_data.get('some_text'))
    # elif req.method == 'GET':
    #    form = TestForm(user=req.user)
    #    print(req.GET)
    form = PostModelForm(req.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.title = "Some random title"
        obj.publish = timezone.now()
        obj.save()
    return render(req, 'form.html', {'form': form})
