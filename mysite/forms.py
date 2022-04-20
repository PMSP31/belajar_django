from django import forms

class FormField(forms.Form):
    # python data type
    int_field = forms.IntegerField(required=False)
    deci_field = forms.DecimalField(required=False)
    float_field = forms.FloatField(required=False)
    bool_field = forms.BooleanField(required=False)
    char_field = forms.CharField(max_length=10)

    # string input
    email_field = forms.EmailField(required=False)
    regex_field = forms.RegexField(regex=r'(P?<test>)',required=False)
    slug_field = forms.SlugField(required=False)
    url_field = forms.URLField(required=False)
    ip_field = forms.GenericIPAddressField(required=False)

    # select field
    option = (
        # ('data', 'yang ditampilkan di View')
        ('A', 'optionA'),
        ('B', 'optionB'),
        ('C', 'optionC'),
    )
    choice_field = forms.ChoiceField(choices=option)
    multi_choice = forms.MultipleChoiceField(choices=option)

    # file field
    file = forms.FileField()
    image = forms.ImageField()