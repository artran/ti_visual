from django import forms
from django.template.defaultfilters import slugify

from models import *

def contact(request):
    _create_form(1)
   if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })
 

def _create_form(form_id):
    contact_form = ContactForm.objects.get(pk=form_id)
    elements = ContactFormElements.objects.filter(form=contact_form).order_by('sort')

    form_name = 'Auto%sForm' % _clean_string(contact_form.name)
    form_str = 'class %s(forms.Form):\n' % form_name
    for element in elements:
        form_str += '    %s = %s\n' % (_clean_string(element.label), element.element.code)

    print(form_str)
    exec(form_str)

def _clean_string(str):
    return slugify(str).replace('-', '_')
