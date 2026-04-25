
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def get_via_uri(self):
        return reverse('api_dispatch_detail', args=['v1', 'gallery', self.id])


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
