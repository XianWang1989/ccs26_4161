
class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

class ImageResource(ModelResource):
    gallery = fields.ForeignKey('your_app.resources.GalleryResource', 'gallery', full=True)

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
