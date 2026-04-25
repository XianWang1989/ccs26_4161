
from tastypie.resources import ModelResource
from tastypie import fields
from .models import Gallery, Image
from tastypie.authorization import Authorization

class GalleryResource(ModelResource):
    images = fields.ToManyField('your_app.resources.ImageResource', 'images', full=True)

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
