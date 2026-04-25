
class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'

    def dehydrate(self, bundle):
        bundle = super(ImageResource, self).dehydrate(bundle)
        # Custom representation can be done here
        return bundle
