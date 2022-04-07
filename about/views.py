from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "app_css":"about/css/styles.css",
        "title" : "About | Interior X",
        "heading" : "About Interior X",
        "content": "Powered By Django",
        "banner": 'about/img/banner_about.png',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ],
    }
    return render(request, 'index.html', context)