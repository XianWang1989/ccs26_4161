
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Gallery, Image

class ImageResource(ModelResource):
    gallery = fields.ForeignKey('gallery_app.resources.GalleryResource', 'gallery')

    class Meta:
        queryset = Image.objects.all()
        resource_name = 'images'
        authorization = Authorization()

class GalleryResource(ModelResource):
    images = fields.ToManyField(ImageResource, 'image_set', full=True)

    class Meta:
        queryset = Gallery.objects.all()
        resource_name = 'gallery'
        authorization = Authorization()
