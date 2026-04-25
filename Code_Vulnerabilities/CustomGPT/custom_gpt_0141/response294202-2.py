
from tastypie.resources import ModelResource
from tastypie import fields
from your_app.models import Gallery, Image  # Adjust the import based on your app name
from tastypie.authorization import Authorization

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'your_app.resources.ImageResource',  # Adjust accordingly
        'images',
        full=True)

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')  # Update this line

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
