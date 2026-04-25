
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        # Return the URI representation of the gallery instance
        from django.urls import reverse
        return reverse('api_dispatch_detail', args=[self.pk], 
                       request=self._request)  # Ensure that you handle self._request properly.


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)


class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'images',
        full=True)

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
