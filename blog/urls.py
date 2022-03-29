from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('story/', views.story),
    path('news/', views.news)
]