
from tastypie.resources import ModelResource
from tastypie import fields
from .models import Gallery, Image
from tastypie.authorization import Authorization

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'images',
        full=True
    )

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

    def dehydrate_gallery(self, bundle):
        if bundle.obj.gallery:
            return {
                'id': bundle.obj.gallery.id,
                'name': bundle.obj.gallery.name,
                'uri': bundle.obj.gallery.get_via_uri()  # Ensure get_via_uri is defined.
            }
        return None
