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
    contact_form = ContactForm()
    context={
        'title' : 'POST',
        'contact_form' : contact_form
    }
    if request.method == 'POST' :
        contact = ContactForm(request.POST)
        if contact.is_valid() :
            ContactModel.objects.create(
                nama_lengkap = request.POST['nama_lengkap'],
                jenis_kelamin = request.POST['jenis_kelamin'],
                # tanggal_lahir = request.POST['tanggal_lahir'],
                email = request.POST['email'],
            )
            return HttpResponseRedirect('/contact/')
    return render(request, 'contact/create.html', context)
