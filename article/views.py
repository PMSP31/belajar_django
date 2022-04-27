from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    # FormView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Article
from .forms import ArticleForm

# Create your views here.
class ArticleListView(ListView):
    model = Article
    # order
    ordering = ['publish']
    # pagination
    paginate_by = 4
    # memberi context
    extra_context = {
        'title' : 'Article | Kelas Terbuka',
        'heading' : "Article",
        'subheading' : 'Article on Kelas Terbuka',
    }

class ArticleDetailView(DetailView):
    model = Article
    extra_context = {
        'title' : 'Detail Article | Kelas Terbuka',
        'heading' : "Detail Article",
        'subheading' : 'Detail Article on Kelas Terbuka',
    }

    def get_context_data(self, **kwargs):
        other_articles = self.model.objects.exclude(slug = self.kwargs['slug'])
        self.extra_context['other_articles'] = other_articles
        return super().get_context_data(**kwargs)

""" class ArticleFormView(FormView):
    form_class = ArticleForm
    template_name = 'article/article_create.html'
    # redirect url if success
    success_url = reverse_lazy('article:index', kwargs={'page':1})
    extra_context = {
        'title' : 'Create Article | Kelas Terbuka',
        'heading' : "Create Article",
        'subheading' : 'Create Article on Kelas Terbuka',
    }

    def form_valid(self, form) :
        form.save()
        return super().form_valid(form) """

# create view menggunakan FormMixin
class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'article/article_create.html'
    extra_context = {
        'title' : 'Create Article | Kelas Terbuka',
        'heading' : "Create Article",
        'subheading' : 'Create Article on Kelas Terbuka',
    }

# create view menggunakan ModelFormMixin
class ArticleCreateModelView(CreateView):
    model = Article
    fields = [
        'title',
        'content',
        'author'
    ]
    extra_context = {
        'title' : 'Create Article Model | Kelas Terbuka',
        'heading' : "Create Article Model",
        'subheading' : 'Create Article Model on Kelas Terbuka',
    }
    # karena menggunakan model maka template yang digunakan article_form, suffix _form

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_create.html'

class ArticleUpdateModel(UpdateView):
    model = Article
    fields = [
        'title',
        'content'
    ]

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article:index', kwargs={'page':1})