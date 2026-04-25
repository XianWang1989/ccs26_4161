
class ImageResource(ModelResource):
    # Change here: Use the 'GalleryResource' instead of 'Gallery'
    gallery = fields.ForeignKey('gallery_app.resources.GalleryResource', 'gallery')

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
