
from django.db import models
from django.core.urlresolvers import reverse  # Import reverse for URL resolution

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return reverse('api_dispatch_detail', kwargs={'resource_name': 'gallery', 'pk': self.pk})

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')  # Use related_name for easier access
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
