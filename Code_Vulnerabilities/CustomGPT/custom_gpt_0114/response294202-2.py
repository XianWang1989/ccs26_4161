
class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')  # Reference to GalleryResource

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
