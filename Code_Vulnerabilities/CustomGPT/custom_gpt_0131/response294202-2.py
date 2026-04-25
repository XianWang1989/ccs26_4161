
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)  # added related_name
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)


class GalleryResource(ModelResource):
    images = fields.ToManyField(
        'gallery_app.resources.ImageResource',
        'images',  # Using the related_name from the Image model
        full=True)

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')  # Ensure you're pointing to GalleryResource

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'
