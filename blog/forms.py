from django import forms

""" class PostForm(forms.Form):
    CATEGORY = (
        ('blog', 'Blog'),
        ('jurnal', 'Jurnal')
    )
    title = forms.CharField(
            max_length=255, 
            widget=forms.TextInput(
                attrs={
                    'class' : 'form-control col-sm-6'
                }
            )
        )
    body = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class' : 'form-control col-sm-6'
                }
            )
        )
    category = forms.ChoiceField(choices=CATEGORY, 
        widget=forms.Select(
            attrs={
                'class' : 'form-control col-sm-6'
            }
    ))

    # validation
    def clean_title(self):
        title_input = self.cleaned_data.get('title')
        
        if title_input == 'Hello World' :
            raise forms.ValidationError("Judul telah ada di model")
        
        return title_input """

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'category'
        ]
        widgets={
            'title' : forms.TextInput(
                attrs={
                    'class' : 'form-control col-sm-6',
                    'placeholder' : 'Input Title Post...'
                }
            ),

            'body' : forms.Textarea(
                attrs={
                    'class' : 'form-control col-sm-6',
                    'placeholder' : 'Input Body Post...'
                }
            ),

            'category' : forms.Select(
                attrs={
                    'class' : 'form-control col-sm-6',
                }
            ),
        }