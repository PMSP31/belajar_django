from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^post/(?P<slugInput>[\w-]+)/$', views.detailPost),
    re_path(r'^category/(?P<categoryInput>[\w-]+)/$', views.categoryPost),
]