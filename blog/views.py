from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView
from .models import Article, Post 
from .forms import PostForm

# Create your views here.
class FilterListView:
    def get_list_data(self, get_request):
        if len(get_request) == 0:
            filter_data = Post.objects.all()
        elif get_request.__contains__('post_category'):
            filter_data = Post.objects.filter(category = get_request['post_category'])
        else:
            filter_data = Post.objects.none()
        return filter_data

class ListPostView(FilterListView, TemplateView):
    template_name = 'blog/index.html'
    context = {
            "app_css" : 'blog/css/styles.css',
            'title' : 'Blog | Kelas Terbuka',
            'heading' : "Blog",
            'subheading' : 'Blog on Kelas Terbuka',
        }

    def get_context_data(self,*args,**kwargs):
        # posts = Post.objects.all()
        posts = self.get_list_data(self.request.GET)
        categories = Post.objects.values_list('category', flat=True).distinct()
        
        self.context['Posts'] = posts
        self.context['Categories'] = categories

        return self.context

class DeletePostView(RedirectView):
    pattern_name = 'blog:index'
    
    def get_redirect_url(self, *args, **kwargs):
        Post.objects.filter(id = kwargs['id_post']).delete()
        return super().get_redirect_url()

class DetailPostView(TemplateView):
    template_name = 'blog/detail.html'
    context = {
        'app_css' : 'blog/css/styles/css',
        'title' : 'Blog'
    }

    def get_context_data(self, *args, **kwargs):
        post = Post.objects.get(slug = kwargs['slug_post'])
        self.context['Post'] = post

        return self.context

class FormPostView(View):
    template_name = 'blog/create.html'
    form = PostForm()
    mode = None
    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'Create Blog | Kelas Terbuka',
        'heading' : "Create Blog",
        'subheading' : 'Create Blog on Kelas Terbuka',
        'post_form' : form
    }

    def get(self, *args, **kwargs):
        # check mode
        if self.mode == 'update':
            update_post = Post.objects.get(id = kwargs['id_post'])
            data_post = update_post.__dict__
            self.form = PostForm(initial = data_post, instance = update_post)

            self.context = {
                'title' : 'Update Blog | Kelas Terbuka',
                'heading' : "Update Blog",
                'subheading' : 'Update Blog on Kelas Terbuka',
                'post_form' : self.form
            }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        if kwargs.__contains__('id_post'):
            # update
            update_post = Post.objects.get(id = kwargs['id_post'])
            self.form = PostForm(self.request.POST, instance = update_post)
        else :
            # create
            self.form = PostForm(self.request.POST)

        if self.form.is_valid():
            self.form.save()
        
        return redirect('blog:index')

class ArticleListView(ListView):
    model = Article
    # order
    ordering = ['publish']
    # pagination
    paginate_by = 2
    # memberi context
    extra_context = {
        'app_css' : 'blog/css/styles.css',
        'title' : 'Article | Kelas Terbuka',
        'heading' : "Article",
        'subheading' : 'Article on Kelas Terbuka',
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)