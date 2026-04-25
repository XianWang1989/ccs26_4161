
from tastypie.resources import ModelResource
from tastypie.fields import ForeignKey, ToManyField
from tastypie.authorization import Authorization
from .models import Gallery, Image

class GalleryResource(ModelResource):
    images = ToManyField(
        'your_app.resources.ImageResource',  # Ensure you replace 'your_app' with the actual app name
        'images',
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = ForeignKey(GalleryResource, 'gallery')  # Use GalleryResource here

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
