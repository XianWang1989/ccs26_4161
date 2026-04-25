
from tastypie.resources import ModelResource
from tastypie import fields
from myapp.models import Gallery, Image  # Adjust the import based on your app name
from tastypie.authorization import Authorization

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'myapp.resources.ImageResource',
        'images',
        full=True,
        null=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        resource_name = 'gallery'
        authorization = Authorization()

class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')

    class Meta:
        queryset = Image.objects.all()
        resource_name = 'images'
        authorization = Authorization()
