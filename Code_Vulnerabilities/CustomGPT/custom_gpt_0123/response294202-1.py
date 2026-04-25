
from tastypie.resources import ModelResource
from tastypie import fields
from gallery_app.models import Gallery, Image
from tastypie.authorization import Authorization

class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'images',
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery', full=True)

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'

    def dehydrate_gallery(self, bundle):
        # Ensure the gallery is serialized correctly
        if bundle.obj.gallery:
            return {
                'id': bundle.obj.gallery.id,
                'name': bundle.obj.gallery.name,
                'api_uri': bundle.obj.gallery.get_via_uri()  # Ensure this returns an appropriate URI
            }
        return None
