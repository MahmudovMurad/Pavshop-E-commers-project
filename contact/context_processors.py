from contact.forms import *
from contact.models import *

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" :
        if  form.is_valid():
            form.save()
    return {'contact_form' : form}