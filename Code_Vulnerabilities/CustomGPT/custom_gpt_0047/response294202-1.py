
from tastypie.resources import ModelResource
from tastypie import fields
from .models import Gallery, Image
from tastypie.authorization import Authorization

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'yourapp.resources.ImageResource',
        'image_set',  # use reverse manager
        full=True)

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery', full=True)

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
