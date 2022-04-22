from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from .models import ContactModel

# Create your views here.
def index(request):
    contact = ContactModel.objects.all()
    context={
        'title': 'Contact | Kelas Terbuka',
        'heading' : 'Contact',
        'subheading' : 'Contact Kelas Terbuka',
        'data_contact' : contact
    }
            
    return render(request, 'contact/index.html', context)

# create ~ get all data form
def create(request):
    contact_form = ContactForm(request.POST)
    context={
        'title' : 'POST',
        'contact_form' : contact_form
    }
    if request.method == 'POST' :
        if contact_form.is_valid() :
            contact_form.save()
            return HttpResponseRedirect('/contact/')
        else :
            error = contact_form.errors
            context['error'] = error
            
    return render(request, 'contact/create.html', context)
