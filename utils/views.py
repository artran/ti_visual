from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from utils.models import *

def contact(request):
    'Take a submitted form, store the content in the db, email the admin and return a message to the user'
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('cms.views.index'))
    
    name= request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    
    if name and email and message:
        contact = Contact.objects.create(name=name, email=email, message=message)
        print contact
    else:
        request.session['warning'] = 'Please fill in all fields'
        request.session['name'] = name
        request.session['email'] = email
        request.session['message'] = message
    return HttpResponseRedirect(reverse('cms.views.index'))

