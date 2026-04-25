
class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')  # Change here

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
