
class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery', full=True)  # Correct the reference to use GalleryResource

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
