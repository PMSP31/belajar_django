from django.shortcuts import render

# method view
def index(request):
    context = {
        'title' : 'Interior X',
        'contributor' : 'Paul Mahardika',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ]
    }
    return render(request, 'index.html', context)