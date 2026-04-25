
class GalleryResource(ModelResource):
    images = fields.ToManyField('your_app.resources.ImageResource', 'images', full=True)

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'
