
class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery', full=True)  # specify GalleryResource

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
        filtering = {
            'gallery': ('exact', 'in'),
        }
