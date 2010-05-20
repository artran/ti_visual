from django.conf.urls.defaults import *

urlpatterns = patterns('utils.views',
    (r'^$', 'contact'),
    (r'^contact-form/$', 'contact'),
)
