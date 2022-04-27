from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','author']
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'class' : 'form-control col-sm-6',
                    'placeholder': 'Title Article...'
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'class' : 'form-control col-sm-6',
                    'placeholder': 'Content Article...'
                }
            ),
            'author' : forms.TextInput(
                attrs={
                    'class' : 'form-control col-sm-6',
                    'placeholder': 'Author Article...'
                }
            ),
        }
