from django.shortcuts import render
from .forms import FormField

# method view
def index(request):
    form_field = FormField()
    context = {
        'title' : 'Home | Kelas Terbuka',
        'heading' : 'Selamat Datang di Kelas Terbuka',
        'subheading' : 'Tempat Belajarnya Programmer Indonesia',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ],
        'form_field' : form_field
    }

    if request.method == 'POST' :
        print(request.POST)
    return render(request, 'index.html', context)