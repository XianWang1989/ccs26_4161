
from django.db import models
from django.core.urlresolvers import reverse
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        return reverse('api_dispatch_detail', kwargs={'resource_name': 'gallery', 'pk': self.pk})

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

class GalleryResource(ModelResource):
    images = fields.ToManyField('gallery_app.resources.ImageResource', 'images', full=True)

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'

class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
