
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Gallery, Image

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'app.resources.ImageResource',
        'image_set',  # Use related_name if defined
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery', full=True)  # Ensure it's related

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
