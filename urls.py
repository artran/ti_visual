import sys
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # The main site
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/articles/section/profile/'}),
    (r'^articles/', include('mingus.urls')),
    (r'^contact/(?P<form_id>\d+)/$', 'ti_visual.contact.views.contact'),
    #(r'^utils/', include('utils.urls')),
)

urlpatterns += patterns('',
    # Admin:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

# Static content
if 'runserver' in sys.argv:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
