
class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'images',
        full=True  # Ensure this is set to true to include all related images
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery', full=True)  # Update here

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
