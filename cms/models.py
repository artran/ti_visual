from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from datetime import datetime

from cms.middleware import threadlocals

class Section(models.Model):
    name = models.CharField(max_length=50, unique=True)
    live = models.BooleanField(default=False)
    slug = models.SlugField(prepopulate_from=('name',), help_text='Auto generated')
    icon_img = models.ImageField(upload_to='icons', help_text='115 x 72 rollover images')
    block_img = models.ImageField(upload_to='block-images', help_text='765 x 253 image')
    sort = models.SmallIntegerField(help_text='Lower number sort earlier.')
    def __str__(self):
        if self.live:
            return self.name
        else:
            return '%s (not live)' % self.name
    class Meta:
        ordering = ['sort']
    class Admin:
        pass

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(help_text='Use html or markdown syntax for the content of the story. For local images use {{ IMAGE[&lt;SLUG&gt;] }} for the url.')
    style = models.TextField('Extra styling', blank=True)
    live_from = models.DateTimeField(blank=True, null=True, default=None, help_text='Blank means live immediately')
    live_to = models.DateTimeField(blank=True, null=True, default=None, help_text='Blank means live until forever')
    feature = models.BooleanField('Featured article', default=False, help_text='Highlighted on section menus')
    home_page = models.BooleanField(default=False, help_text='Goes on the home page for a section')
    created_at = models.DateTimeField(blank=True, editable=False)
    created_by = models.ForeignKey(User, editable=False)
    last_edited_at = models.DateTimeField(blank=True, editable=False)
    last_edited_by = models.ForeignKey(User, related_name='edited_articles', editable=False)
    related = models.ManyToManyField('self', filter_interface=models.HORIZONTAL, blank=True)
    slug = models.SlugField(prepopulate_from=('title',), unique=True, help_text='Auto generated')
    section = models.ForeignKey(Section, related_name='articles')
    def is_live(self):
        'Returns True if now is between live_from and live_to'
        now = datetime.now()
        return (self.live_from is None or self.live_from < now) and (self.live_to is None or self.live_to > now)
    
    # Set the creator and last_edited_by when appropriate
    def save(self):
        # If the object already existed, it will already have an id
        if not self.id:
            # This is a new object, set the creator 
            self.created_by = threadlocals.get_current_user()
            self.created_at = datetime.now()
        # All articles need the edited by and edited at fields setting
        self.last_edited_by = threadlocals.get_current_user()
        self.last_edited_at = datetime.now()
        super(Article, self).save()
        
    def __str__(self):
        if self.is_live():
            return self.title
        else:
            return '%s (not live)' % self.title
    class Admin:
        save_on_top = True
        list_filter = ('section', 'created_by')
        search_fields = ('title',)
        list_display = ('title', 'live_from', 'live_to', 'is_live')
    
class Image(models.Model):
    name = models.CharField(max_length=30, core=True)
    slug = models.SlugField(prepopulate_from=('name',), blank=True, help_text='Auto generated but can be overridden')
    caption = models.CharField(max_length=50, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='cms_images', width_field='width', height_field='height', core=True)
    created_at = models.DateTimeField(blank=True, editable=False)
    created_by = models.ForeignKey(User, editable=False)
    
    # Set the creator fields when appropriate
    def save(self):
        # If the object already existed, it will already have an id
        if not self.id:
            # This is a new object, set the creator 
            self.created_by = threadlocals.get_current_user()
            self.created_at = datetime.now()
        
        # Set a slug if one isn't already set
        if not self.slug:
            self.slug = slugify(self.name)
        super(Image, self).save()
        
    def get_absolute_url(self):
        return '/media/%s' % self.get_image_url()
    def __str__(self):
        return self.name
    class Admin:
        pass
    class Meta:
        abstract = True
    #    unique_together = (('slug', 'article'),)

class ArticleImage(Image):
    article = models.ForeignKey(Article, edit_inline=models.STACKED, related_name='images')
    # I've comented this out after creation of the tables because it breaks the inline-editing in Articles.
    # As the uniqueness test is done in the db this shouldn't be an issue.
    class Meta:
        unique_together = (('slug', 'article'),)

class SectionImage(Image):
    section = models.ForeignKey(Section, edit_inline=models.STACKED, related_name='images')
    # I've comented this out after creation of the tables because it breaks the inline-editing in Articles.
    # As the uniqueness test is done in the db this shouldn't be an issue.
    class Meta:
        unique_together = (('slug', 'section'),)
    