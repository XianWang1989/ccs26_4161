
from django.db import models
from django.core.urlresolvers import reverse

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        """
        This method returns the URI that can be used to access this
        Gallery instance through the Tastypie API.
        """
        return reverse('api_dispatch_detail', kwargs={
            'resource_name': 'gallery',
            'pk': self.id
        })


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')  # Always good to use related_name for clarity
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
