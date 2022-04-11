from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title" : "About | Kelas Terbuka",
        "heading" : "About Kelas Terbuka",
        "subheading": "Powered By Django",
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ],
    }
    return render(request, 'about/index.html', context)