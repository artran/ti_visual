import sys
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # The main site
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/articles/'}),
    (r'^articles/', include('cms.urls')),
    (r'^utils/', include('utils.urls')),
)

urlpatterns += patterns('',
    # Admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)

# Static content
if 'runserver' in sys.argv:
    urlpatterns += patterns('',
        (r'^media/css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/css'}),
        (r'^media/js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/js'}),
        (r'^media/images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/images'}),
        (r'^media/cms_images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/cms_images'}),
        (r'^media/icons/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/icons'}),
        (r'^media/block-images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/block-images'}),
    )