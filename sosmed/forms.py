from django import forms
from .models import Sosmed

class SosmedForm(forms.ModelForm):
    class Meta:
        model = Sosmed
        fields = [
            'first_name',
            'last_name',
            'username',
            'content'
        ]