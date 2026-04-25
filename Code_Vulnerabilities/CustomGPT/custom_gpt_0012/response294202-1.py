
# models.py
from django.urls import reverse

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        # Return the URL for this Gallery object
        return reverse('api_dispatch_detail', args=[self.pk])
