from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.createPost, name='create'),
    path('delete/<int:id_post>',views.deletePost, name='delete'),
    path('update/<int:id_post>',views.updatePost, name='update'),
    re_path(r'^post/(?P<slugInput>[\w-]+)/$', views.detailPost, name='detail'),
    re_path(r'^category/(?P<categoryInput>[\w-]+)/$', views.categoryPost, name='category'),
]