
from tastypie.resources import ModelResource
from tastypie import fields
from your_app.models import Gallery, Image  # Adjust according to your app structure

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'your_app.resources.ImageResource',  # Adjust based on your app name
        'images',
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        resource_name = 'gallery'
        authorization = Authorization()


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')  # Use GalleryResource

    class Meta:
        queryset = Image.objects.all()
        resource_name = 'images'
        authorization = Authorization()
