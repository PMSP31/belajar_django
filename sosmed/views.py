from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from .models import Sosmed
from .forms import SosmedForm
from django.shortcuts import render, redirect

# Create your views here.

# filter handler
class FilterListView:
    def get_list_data(self, get_request):
        if len(get_request) == 0:
            filter_data = Sosmed.objects.all()
        elif get_request.__contains__('user_content'):
            filter_data = Sosmed.objects.filter(content = get_request['user_content'])
        else:
            filter_data = Sosmed.objects.none()
        return filter_data

        
class ListView(FilterListView, TemplateView):
    template_name = 'sosmed/index.html'

    def get_context_data(self, **kwargs) :
        sosmeds = self.get_list_data(self.request.GET)
        list_contents = Sosmed.objects.values_list('content', flat=True).distinct()

        context = {
            'title' : 'Sosmed | Kelas Terbuka',
            'heading' : 'Social Media',
            'sosmeds' : sosmeds,
            'list_contents' : list_contents
        }

        return context

class DeleteView(RedirectView) :
    pattern_name = 'sosmed:index'

    def get_redirect_url(self, *args, **kwargs):
        Sosmed.objects.filter(id=kwargs['delete_id']).delete() 
        return super().get_redirect_url()

class SosmedFormView(View):
    template_name = 'sosmed/create.html'
    form = SosmedForm()
    mode = None
    context = {
        'title' : 'Tambah Akun',
        'sosmed_form' : form
        }

    def get(self, *args, **kwargs):
        # mode = update
        if self.mode == 'update':
            # get sosmed by id
            sosmed_update = Sosmed.objects.get(id = kwargs['update_id'])
            # get data sosmed
            data = sosmed_update.__dict__
            # form for update
            self.form = SosmedForm(initial=data, instance=sosmed_update)
            # context for update
            self.context = {
                'title' : 'Update Akun',
                'sosmed_form' : self.form
            }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        if kwargs.__contains__('update_id'):
            # update
            sosmed_update = Sosmed.objects.get(id = kwargs['update_id'])
            self.form = SosmedForm(self.request.POST, instance=sosmed_update)
        else:
            # create
            self.form = SosmedForm(self.request.POST)
        
        if self.form.is_valid():
            self.form.save()

        return redirect('sosmed:index')
