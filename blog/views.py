from django.shortcuts import render
from .models import Post # import model

# Create your views here.
def index(request):
    # queryset
    # posts = Post.objects.all() # ambil semua Post
    posts = Post.objects.filter(author__iexact="Paul")
    # print(posts)

    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'Blog | Kelas Terbuka',
        'heading' : "Blog",
        'subheading' : 'Blog on Kelas Terbuka',
        'Posts' : posts
    }
    return render(request, "blog/index.html", context)