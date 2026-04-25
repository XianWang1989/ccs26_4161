
class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'image_set',  # This assumes a reverse relationship based on the ForeignKey.
        full=True
    )

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'
