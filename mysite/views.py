from django.shortcuts import render

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
        "banner": 'img/banner_home.png',
    }
    return render(request, 'index.html', context)