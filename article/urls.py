from django.urls import path
from .views import ArticleListView, DetailArticleView

app_name = 'article'
urlpatterns = [
    path('<int:page>', ArticleListView.as_view(), name='index'),
    path('detail/<slug:slug>',DetailArticleView.as_view(), name='detail')
]