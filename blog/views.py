from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'Interior X',
        'contributor' : 'Rudi'
    }
    return render(request, "blog/index.html", context)

def story(request):
    context = {
        'title' : 'Story',
        'contributor' : 'Yanto'
    }
    return render(request, "blog/index.html", context)

def news(request):
    context = {
        'title' : 'News',
        'contributor' : 'Joko'
    }
    return render(request, "blog/index.html", context)