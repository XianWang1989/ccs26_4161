
class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery', full=True)

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'

    def dehydrate_gallery(self, bundle):
        # Ensure that the gallery is being serialized correctly
        if bundle.obj.gallery:
            return bundle.obj.gallery.get_via_uri()
        return None
