
from django.db import models
from django.core.urlresolvers import reverse  # For generating URLs

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        return reverse('api_dispatch_detail', kwargs={'resource_name': 'gallery', 'pk': self.pk})
