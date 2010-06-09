from django.shortcuts import render_to_response

from forms import ContactForm
from models import *


def contact(request, form_id):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(form_id, request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm(form_id) # An unbound form

    return render_to_response('contact/contact.html', {
        'form': form,
    })


def list_forms(request):
    pass
