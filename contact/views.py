from django import forms
from django.template.defaultfilters import slugify

from models import *

def contact(request):
    _create_form(1)

def _create_form(form_id):
    contact_form = ContactForm.objects.get(pk=form_id)
    elements = ContactFormElements.objects.filter(form=contact_form).order_by('sort')

    form_str = 'class Auto%sForm(forms.Form):\n' % _clean_string(contact_form.name)
    for element in elements:
        form_str += '    %s = %s\n' % (_clean_string(element.label), element.element.code)

    print(form_str)
    exec(form_str)

def _clean_string(str):
    return slugify(str).replace('-', '_')
