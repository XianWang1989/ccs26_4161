
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Gallery, Image

class ImageResource(ModelResource):
    gallery = fields.ForeignKey('gallery_app.resources.GalleryResource', 'gallery', related_name='images')

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'images',
        full=True,
        null=True  # Allow for no images
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'
