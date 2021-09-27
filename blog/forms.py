from django import forms
from .models import Post


'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             default=1, on_delete=models.SET_NULL,
                             blank=True,
                             null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.FileField(upload_to=upload_location,
                             null=True,
                             blank=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
'''


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'slug', 'image']
        #exclude = ['height_field']

        def clean_title(self, *args, **kwargs):
            title = self.cleaned_data.get('title')
            print(title)
            raise forms.ValidationError('nope')
            # return title


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
