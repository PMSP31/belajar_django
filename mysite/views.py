from django.shortcuts import render

# method view
def index(request):
    context = {
        'title' : 'Home | Interior X',
        'heading' : 'Welcome To Interior X',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ],
        "banner": 'img/banner_home.png',
    }
    return render(request, 'index.html', context)