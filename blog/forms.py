from django import forms


class SearchForm(forms.Form):
    q = forms.CharField()


class TestForm(forms.Form):
    some_text = forms.CharField()
    boolean = forms.BooleanField(required=False)
    integer = forms.IntegerField(initial=100)
    email = forms.EmailField()

    def __init__(self, user=None, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['some_text'].initial = user.username

    def clean_integer(self, *args, **kwargs):
        ''' clean_[field_name] '''
        integer = self.cleaned_data.get('integer')
        if integer < 10:
            raise forms.ValidationError('The integer must be greater than 10')
        # return integer
        return 101

    def clean_some_text(self, *args, **kwargs):
        some_text = self.cleaned_data.get('some_text')
        if len(some_text) < 10:
            raise forms.ValidationError(
                'Ensure the text is greater than 10 characters')
        return some_text
