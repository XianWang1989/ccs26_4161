
class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')  # Ensure this points to the correct resource

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
