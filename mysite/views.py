from django.shortcuts import render
from django.http import HttpResponse

# method view
def index(request):
    context = {
        'title' : 'Home | Kelas Terbuka',
        'heading' : 'Selamat Datang di Kelas Terbuka',
        'subheading' : 'Tempat Belajarnya Programmer Indonesia',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ],
    }
    return render(request, 'index.html', context)

def number(request, input):
    heading = f"<h1>Page-{input}</h1>"
    return HttpResponse(heading)

def date(request, year, month, day):
    heading = f"Date : {year} / {month} / {day}"
    return HttpResponse(heading)