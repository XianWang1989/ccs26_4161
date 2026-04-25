
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Gallery, Image

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'your_app.resources.ImageResource',  # Ensure this points to the correct import path
        'image_set',  # Use 'image_set' to reference the related images
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')  # Use GalleryResource here

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
