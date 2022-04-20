from django.shortcuts import render, redirect
from .models import Post # import model
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
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

def createPost(request):
    post_form = PostForm(request.POST)
    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'Create Blog | Kelas Terbuka',
        'heading' : "Create Blog",
        'subheading' : 'Create Blog on Kelas Terbuka',
        'post_form' : post_form
    }

    if request.method == 'POST' :
        if post_form.is_valid():
            """ Post.objects.create(
                title = post_form.cleaned_data.get('title'),
                body = post_form.cleaned_data.get('body'),
                category = post_form.cleaned_data.get('category'),
            ) """
            post_form.save()
            return redirect('blog:index')
        else :
            error = post_form.errors
            context['error'] = error

    return render(request, "blog/create.html", context)

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