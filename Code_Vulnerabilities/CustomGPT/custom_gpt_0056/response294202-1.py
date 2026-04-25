
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Gallery, Image

class ImageResource(ModelResource):
    gallery = fields.ForeignKey('your_app_name.resources.GalleryResource', 'gallery')

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'


class GalleryResource(ModelResource):
    images = fields.ToManyField(
        ImageResource,  # Use the ImageResource directly
        'images',
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'
