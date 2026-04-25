
class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')  # Corrected line

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
