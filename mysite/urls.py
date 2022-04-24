"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import ContextParams, ContextView, RedirectParams, index,IndexView
# import template view pada urls.py
from django.views.generic.base import TemplateView, RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/', include('about.urls', namespace='about')),
    path('contact/', include('contact.urls', namespace='contact')),
    # mendaftarkan class based view ke urls.py
    path('class/', IndexView.as_view(template_name='index2.html')),
    # TemplateView untuk statis
    path('default/', TemplateView.as_view(template_name = 'default.html')),
    # ContextView
    path('context/', ContextView.as_view()),
    # context params
    path('params/<int:param1>/<str:param2>', ContextParams.as_view(), name='params'),
    # RedirectView
    # path('redirect/', RedirectView.as_view(pattern_name='blog:create'), name='redirect') # dengan pattern_name
    path('redirect/', RedirectView.as_view(url='/blog'), name='redirect'), # dengan url
    # redirect with params
    path('redirectpar/<int:param1>/<str:param2>', RedirectParams.as_view(), name='redirectpar')
]

# Bisa mendaftarkan langsung TemplateView pada urls.py ketika, page yang dibuat bersifat statis/tidak ada perubahan apapun.

