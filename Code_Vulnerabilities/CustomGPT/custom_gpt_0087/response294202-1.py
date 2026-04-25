
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Gallery, Image

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'your_app.resources.ImageResource',
        'image_set',  # Make sure this matches the manager for related images
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        resource_name = 'gallery'
        authorization = Authorization()


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery', full=True)  # Link to GalleryResource

    class Meta:
        queryset = Image.objects.all()
        resource_name = 'images'
        authorization = Authorization()
