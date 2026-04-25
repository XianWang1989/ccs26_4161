
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'your_app.resources.ImageResource',
        'image_set',  # Make sure this matches the related name in the Image model
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
