from django.shortcuts import render

# method view
def index(request):
    context = {
        'title' : 'Interior X',
        'contributor' : 'Paul Mahardika'
    }
    return render(request, 'index.html', context)