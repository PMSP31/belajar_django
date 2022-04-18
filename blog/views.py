from django.shortcuts import render
from .models import Post # import model
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.all()
    # categories
    categories = Post.objects.values('category').distinct()

    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'Blog | Kelas Terbuka',
        'heading' : "Blog",
        'subheading' : 'Blog on Kelas Terbuka',
        'Posts' : posts,
        'Categories': categories
    }
    return render(request, "blog/index.html", context)

def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category = categoryInput)
    categories = Post.objects.values('category').distinct()
    context = {
        "app_css" : 'blog/css/styles.css',
        "title" : "Blog",
        'Posts' : posts,
        'Categories': categories
    }
    return render(request, "blog/category.html", context)

def detailPost(request, slugInput):
    post = Post.objects.get(slug = slugInput)
    context = {
        "app_css" : 'blog/css/styles.css',
        "title" : "Blog",
        'Post' : post
    }
    return render(request, "blog/detail.html", context)