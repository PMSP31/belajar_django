from django.shortcuts import render

# method view ~ function based view
def index(request):
    context = {
        'title' : 'Home | Kelas Terbuka',
        'heading' : 'Selamat Datang di Kelas Terbuka',
        'subheading' : 'Tempat Belajarnya Programmer Indonesia',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ],
    }
    return render(request, 'index.html', context)

# class based view
from django.views.generic.base import TemplateView, RedirectView

""" 
    dalam TemplateView menginherits:
    ~ TemplateResponseMixin
    ~ ContextMixin
    ~ View
"""
class IndexView(TemplateView):
    pass

# context
class ContextView(TemplateView):
    template_name = 'context.html'

    # memberi context pada class view
    def get_context_data(self) :
        context = {
            'judul' : 'Context Pada Class',
            'penulis' : 'Paul Mahardika'
        }
        return context

# context parameter
class ContextParams(TemplateView):
    template_name = 'params.html'

    def get_context_data(self, *args, **kwargs) :
        # context = kwargs
        print(kwargs)
        if self.request.GET.__contains__('tipe'):
            kwargs['tipe'] = self.request.GET['tipe']
        print(kwargs)
        context = super().get_context_data(*args ,**kwargs)
        context['judul'] = 'Context with params'
        context['user'] = 'Paul Mahardika'

        return context

# RedirectView with parameter
class RedirectParams(RedirectView) : 
    pattern_name = 'params'
    permanent = False
    query_string = True # mengirim query, default False

    # merubah data dari parameter
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        if kwargs['param1'] == 16 :
            print('merubah param2')
            kwargs['param2'] = 'Rudi'
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)