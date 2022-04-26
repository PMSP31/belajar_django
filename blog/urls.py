from django.urls import path
from .views import ListPostView, FormPostView, DeletePostView, DetailPostView, ArticleListView

app_name = 'blog'
urlpatterns = [
    path('', ListPostView.as_view(), name='index'),
    path('create/',FormPostView.as_view(), name='create'),
    path('delete/<int:id_post>',DeletePostView.as_view(), name='delete'),
    path('update/<int:id_post>',FormPostView.as_view(mode='update'), name='update'),
    path('post/<slug:slug_post>/', DetailPostView.as_view(), name='detail'),
    path('article/<int:page>', ArticleListView.as_view(), name='article'),
]