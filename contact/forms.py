from django import forms

# create form by django
""" class ContactForm(forms.Form):
    GENDER = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan')
    )
    TAHUN = range(1945, 2022, 1)

    nama_lengkap = forms.CharField(
            label='Nama Lengkap', 
            max_length=50,
            widget=forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Masukan Nama Lengkap Anda...'
                }
            )
        )
    jenis_kelamin = forms.ChoiceField(
            choices=GENDER, 
            widget=forms.RadioSelect(
                attrs={
                    'class' : 'form-check-input'
                }
            )
        )
    tanggal_lahir = forms.DateField(
            widget=forms.SelectDateWidget(
                    years=TAHUN,
                    attrs={
                        'class' : 'form-control col-sm-2'
                    }
                )
        )
    email = forms.EmailField(
            label='Email',
            widget=forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Masukan Email Anda...'
                }
            )
        )
    agree = forms.BooleanField(
            label="Simpan Data",
            widget=forms.CheckboxInput(
                attrs={
                    'class' : 'form-check-input'
                }
            )
        ) """

from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields=[
            'nama_lengkap',
            'jenis_kelamin',
            'tanggal_lahir',
            'email'
        ]
        TAHUN = range(1945, 2022, 1)
        widgets={
            'nama_lengkap' : forms.TextInput(
                attrs={
                    'class' : 'form-control col-sm-6',
                    'placeholder' : 'Masukan Nama Lengkap Anda'
                }
            ),
            'jenis_kelamin' : forms.Select(
                attrs={
                    'class' : 'form-control col-sm-6'
                }
            ),
            'tanggal_lahir' : forms.SelectDateWidget(
                years=TAHUN,
                attrs={
                    'class' : 'form-control col-sm-6'
                }
            ),
            'email' : forms.TextInput(
                attrs={
                    'class' : 'form-control col-sm-6',
                    'placeholder' : 'Masukan Email Anda...'
                }
            )
        }