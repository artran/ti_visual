from django.db import models

class Element(models.Model):
    'A component of a contact form.'
    
    name = models.CharField(max_length=20, help_text='Memorable name for the component')
    code = models.CharField(max_length=100, help_text='The django code to produce this component')
    
    def __unicode__(self):
        return self.name

class ContactForm(models.Model):
    'A collection of form elements that know where to post to.'
    
    name = models.CharField(max_length=20, help_text='Memorable name for the form.')
    recipient_list = models.TextField(help_text='Comma separated list of recipients.')
    subject_template = models.CharField(max_length=100, help_text='Template code to produce the email subject line.')
    body_template = models.TextField(help_text='Template code to produce the email body.')
    elements = models.ManyToManyField(Element, related_name='form', through='ContactFormElements')
    
    def __unicode__(self):
        return self.name

class ContactFormElements(models.Model):
    'A join model that allows the elements of a form to be ordered.'
    
    element = models.ForeignKey(Element)
    form = models.ForeignKey(ContactForm)
    sort = models.PositiveSmallIntegerField(help_text='Low numbers sort first.')
    label = models.CharField(max_length=100, help_text='Label for this element.')