
from tastypie.resources import ModelResource
from tastypie import fields
from myapp.models import Gallery, Image  # Adjust import according to your app structure

class GalleryResource(ModelResource):
    images = fields.ToManyField('myapp.resources.ImageResource', 'images', full=True)

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
