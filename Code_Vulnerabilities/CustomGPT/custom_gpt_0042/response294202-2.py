
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from .models import Gallery, Image

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'yourapp.resources.ImageResource',  # Update this to your correct app name
        'images',
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        resource_name = 'gallery'
        authorization = Authorization()


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery', full=True)

    class Meta:
        queryset = Image.objects.all()
        resource_name = 'images'
        authorization = Authorization()
