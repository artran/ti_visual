from django.shortcuts import render_to_response

from models import *
from forms import ContactForm

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(1, request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm(1) # An unbound form
    
    #assert 0, dir(form)

    return render_to_response('contact/contact.html', {
        'form': form,
    })