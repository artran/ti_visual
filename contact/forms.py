from django import forms
from django.template.defaultfilters import slugify

from models import *


class ContactForm(forms.Form):
    def __init__(self, form_id, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        
        contact_form = ContactFormModel.objects.get(pk=form_id)
        elements = ContactFormElements.objects.filter(form=contact_form).order_by('sort')

        for element in elements:
            el_type = element.element.field

            if el_type == 'char':
                field = forms.CharField(max_length=25)
            elif el_type == 'email':
                field = forms.EmailField()
            elif el_type == 'bool':
                field = forms.BooleanField()
            elif el_type == 'date':
                field = forms.DateField()
            elif el_type == 'dec':
                field = forms.DecimalField()
            elif el_type == 'int':
                field = forms.IntegerField()
            else:
                raise NotImplementedError, 'Contact form element of type %s is not implemented' % el_type

            field.required = element.required
            field.label = element.label
            
            self.fields['%s' % _clean_string(element.label)] = field


def _clean_string(str):
    return slugify(str).replace('-', '_')