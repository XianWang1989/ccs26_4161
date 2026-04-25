
from tastypie.resources import ModelResource
from tastypie import fields
from gallery_app.models import Gallery, Image
from tastypie.authorization import Authorization

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'image_set',  # Changed to 'image_set' for the reverse relation
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')  # Ensure correct reference

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
