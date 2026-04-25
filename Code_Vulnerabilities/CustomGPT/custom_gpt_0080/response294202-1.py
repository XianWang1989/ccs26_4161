
from django.db import models
from django.core.urlresolvers import reverse  # import reverse to build URLs

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        return reverse('api_dispatch_detail', args=[self._meta.app_label, 'gallery', self.id])

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
