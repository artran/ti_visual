# Django settings for tivisual project.
import os

DIRNAME = os.path.dirname(__file__)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(DIRNAME, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
)

SECTION_BLOCK_IMG_HELP = 'The large image on each section. Needs to be 765 x 253'
SECTION_THUMB_IMG_HELP = 'The section icon. Use a rollover image of 115 x 72'
ARTICLE_IMG_HELP = 'Must be an image.'
SECTION_ALT_IMG_HELP = 'An alternative for the large image on each section so it needs to be 765 x 253.'
SECTION_ALT_THUMB_IMG_HELP = 'Not used - leave blank'

# Load the local settings
from local_settings import *
