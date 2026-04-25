
class ImageResource(ModelResource):
    gallery = fields.ForeignKey(
        'gallery_app.resources.GalleryResource',  # Updated line
        'gallery'
    )

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
