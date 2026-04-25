
# models.py
from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('api_dispatch_list', kwargs={'resource_name': 'gallery'})

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

# resources.py
from tastypie.resources import ModelResource
from tastypie import fields
from gallery_app.models import Gallery, Image

class GalleryResource(ModelResource):
    images = fields.ToManyField('gallery_app.resources.ImageResource', 'images', full=True)

    class Meta:
        queryset = Gallery.objects.all()
        resource_name = 'gallery'
        authorization = Authorization()

class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')

    class Meta:
        queryset = Image.objects.all()
        resource_name = 'images'
        authorization = Authorization()
