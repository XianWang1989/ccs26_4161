
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from .models import Gallery, Image

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'your_app_name.resources.ImageResource',
        'image_set',  # Use image_set to reference related images
        full=True
    )

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
