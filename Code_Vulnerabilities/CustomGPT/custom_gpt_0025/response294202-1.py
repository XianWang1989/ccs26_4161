
# resources.py

from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Gallery, Image

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'image_set',  # Use 'image_set' to access related images
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'

    def get_via_uri(self):
        return self.get_resource_uri()

class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
