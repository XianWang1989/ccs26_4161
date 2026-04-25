
from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        return "/api/v1/gallery/%d/" % self.id

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')  # Ensure the related_name is set
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
