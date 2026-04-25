
# models.py
from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def get_via_uri(self):
        return reverse('api_dispatch_detail', kwargs={'resource_name': 'gallery', 'pk': self.pk})

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')  # Use related_name for easier access
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

# resources.py
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields

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
