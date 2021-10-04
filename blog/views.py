#from django.forms.formsets import formset_factory
from django.http import request
from django.shortcuts import render
from django.utils import timezone
from django.forms import formset_factory, modelformset_factory

from .forms import SearchForm, TestForm, PostModelForm
from .models import Post


def formset_view(req):
    PostModelFormset = modelformset_factory(
        Post,
        fields=['user', 'title', 'slug', 'image'],
        # extra=2
    )
    formset = PostModelFormset(req.POST or None)

    if formset.is_valid():
        # formset.save(commit=False)
        # for form in formset:
        #    print(form.cleaned_data)
        for form in formset:
            obj = form.save(commit=False)
            obj.publish = timezone.now()
            form.save()

    context = {
        'formset': formset
    }
    return render(req, 'formset_view.html', context)

# def formset_view(req):
#    TestFormset = formset_factory(TestForm)
#    formset = TestFormset(req.POST or None)

#    if formset.is_valid():
#        for form in formset:
#            print(form.cleaned_data)

#    context = {
#        'formset': formset
#    }
#    return render(req, 'formset_view.html', context)


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

    if form.has_error:
        # print(form.errors.as_json())
        # print(form.errors.as_text())

        data = form.errors.items()
        for key, value in data:
            #print(key, value)
            # print(dir(value))

            error_str = f"{key}: {value.as_text()}"
            print(error_str)
        print(dir(form.errors))

    return render(req, 'form.html', {'form': form})
