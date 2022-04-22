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
            post_form.save()
            return redirect('blog:index')
        else :
            error = post_form.errors
            context['error'] = error

    return render(request, "blog/create.html", context)

def deletePost(request, id_post):
    # filter data by id, delete data from id
    Post.objects.filter(id = id_post).delete()
    return redirect('blog:index')

def updatePost(request, id_post):
    # get post by id
    update_post = Post.objects.get(id = id_post)
    # get data post from id
    data_post = {
        "title" : update_post.title,
        "body" : update_post.body,
        "categoory" : update_post.category,
    }
    post_form = PostForm(request.POST or None, initial = data_post, instance = update_post)

    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'Update Blog | Kelas Terbuka',
        'heading' : "Update Blog",
        'subheading' : 'Update Blog on Kelas Terbuka',
        'post_form' : post_form
    }

    if request.method == 'POST' :
        if post_form.is_valid():
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