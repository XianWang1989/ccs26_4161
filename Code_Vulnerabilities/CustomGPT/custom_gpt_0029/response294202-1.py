
from django.db import models
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        return "/api/v1/gallery/{}/".format(self.id)


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
