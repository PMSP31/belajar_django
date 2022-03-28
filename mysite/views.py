# from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    # render template index
    return render(request, 'index.html')