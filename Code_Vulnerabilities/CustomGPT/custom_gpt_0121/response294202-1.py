
from django.db import models
from django.core.urlresolvers import reverse

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('api_dispatch_detail', args=[self.pk], resource_name='gallery']

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
