from django import forms

from models import *


class DynForm(forms.Form):
    def __init__(form_id, *args, **kwargs):
        contact_form = ContactForm.objects.get(pk=form_id)
        elements = ContactFormElements.objects.filter(form=contact_form).order_by('sort')

        for element in elements:
            pass
