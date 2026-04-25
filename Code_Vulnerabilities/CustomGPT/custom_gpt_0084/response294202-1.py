
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Gallery, Image

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'yourapp.resources.ImageResource',  # Replace 'yourapp' with the actual app name
        'images',
        full=True
    )

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
