
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from gallery_app.models import Gallery, Image

class ImageResource(ModelResource):
    gallery = fields.ForeignKey('gallery_app.resources.GalleryResource', 'gallery')

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'

class GalleryResource(ModelResource):
    images = fields.ToManyField(ImageResource, 'image_set', full=True)

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'
