from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def index(request):
    contact_form = ContactForm()
    context={
        'title': 'Contact | Kelas Terbuka',
        'heading' : 'Contact',
        'subheading' : 'Contact Kelas Terbuka',
        'contact_form' : contact_form
    }
    # get data from contact_form
    if request.method == "POST":
        form = ContactForm(request.POST)
        # check if form is valid data
        if form.is_valid():
            print(request.POST)
            # context['nama'] = request.POST['nama']
            # context['email'] = request.POST['email']
            
    return render(request, 'contact/index.html', context)