
class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')

    class Meta:
        queryset = Image.objects.all()
        resource_name = 'images'
        authorization = Authorization()
        # Add other settings if needed
