
class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'images',  # This should match the related_name from the Image model
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery', full=True)  # Use GalleryResource directly

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
