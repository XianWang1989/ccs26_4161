
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Gallery, Image

class ImageResource(ModelResource):
    gallery = fields.ForeignKey('gallery_app.resources.GalleryResource', 'gallery', full=True)

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'

class GalleryResource(ModelResource):
    images = fields.ToManyField('gallery_app.resources.ImageResource', 'image_set', full=True)

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'
