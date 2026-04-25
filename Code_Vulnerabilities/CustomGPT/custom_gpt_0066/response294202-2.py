
from django.urls import reverse
from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return reverse('api_dispatch_detail', args=[self._meta.app_label, 'gallery', self.pk])
