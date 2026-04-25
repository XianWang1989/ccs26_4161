
# models.py
from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def get_via_uri(self):
        from django.core.urlresolvers import reverse
        return reverse('api_dispatch_detail', kwargs={'resource_name': 'gallery', 'pk': self.pk})

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
