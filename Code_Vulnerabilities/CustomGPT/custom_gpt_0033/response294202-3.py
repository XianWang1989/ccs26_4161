
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Gallery, Image

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'images',
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(
        'gallery_app.resources.GalleryResource',  # Reference the correct resource
        'gallery'
    )

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
