from django.contrib import admin
from ti_visual.contact.models import *

class ElementAdmin(admin.ModelAdmin):
    pass

class FormElementInline(admin.TabularInline):
    model = ContactFormElements
    extra = 2

class ContactFormAdmin(admin.ModelAdmin):
    inlines = (FormElementInline,)

admin.site.register(Element, ElementAdmin)
admin.site.register(ContactForm, ContactFormAdmin)