
from django.db import models
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        # Return the URI for this gallery instance
        from tastypie.api import Api
        api = Api(api_name='v1')
        return api.get_resource_uri(GalleryResource(), self)

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
