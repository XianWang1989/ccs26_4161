
from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.title)
