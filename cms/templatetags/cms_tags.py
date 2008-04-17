from django import template

import re

from cms.models import Image

image_match_regex = re.compile(r'{{\s*IMAGE\[[\w-]*\]\s*}}')
slug_match_regex = re.compile(r'\[([\w-]*)\]')

register = template.Library()

@register.filter
def add_images(article):
    '''
    Goes through the article body text resolving {{ IMAGE[<SLUG>] }} into the correct url for the image
    with slug=<SLUG>
    '''
    body = article.body
    matches = image_match_regex.finditer(body)
    if matches:
        images = article.images.all()
        
        # To manipulate the body text safely we need to reverse the iterator
        for match in reversed(list(matches)):
            slug = slug_match_regex.search(match.group()).group(1)
            try:
                image = images.get(slug=slug)
                image_url = image.get_absolute_url()
            except AssertionError:
                print 'Multiple images found with the slug %s' % slug
                image_url = 'MultipleImagesExist'
            except Image.DoesNotExist:
                print 'No images with the slug "%s" related to article with slug "%s"' % (slug, article.slug)
                image_url = 'NoImageFound'
            
            body = body[:match.start()] + image_url + body[match.end():]
    return body
add_images.is_safe = True
