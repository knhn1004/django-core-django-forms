from django import forms


class SearchForm(forms.Form):
    q = forms.CharField()


SOME_CHOICES = (
    ('db-value', 'Display Value'),
    ('db-value-2', 'Display Value 2'),
    ('db-value-3', 'Display Value 3'),
)

INT_CHOICES = [tuple([x, x]) for x in range(0, 100)]


YEARS = [x for x in range(1980, 2031)]


class TestForm(forms.Form):
    date_field = forms.DateField(
        widget=forms.SelectDateWidget(years=YEARS), initial="2020-11-20")
    some_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 10
        }),
        label='text'
    )
    choices = forms.CharField(
        widget=forms.Select(choices=SOME_CHOICES)
    )
    boolean = forms.BooleanField(required=False)
    integer = forms.IntegerField(
        initial=100, widget=forms.RadioSelect(choices=INT_CHOICES))
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
