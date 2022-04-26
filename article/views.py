from django.views.generic import ListView, DetailView
from .models import Article


# Create your views here.
class ArticleListView(ListView):
    model = Article
    # order
    ordering = ['publish']
    # pagination
    paginate_by = 2
    # memberi context
    extra_context = {
        'title' : 'Article | Kelas Terbuka',
        'heading' : "Article",
        'subheading' : 'Article on Kelas Terbuka',
    }

class DetailArticleView(DetailView):
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