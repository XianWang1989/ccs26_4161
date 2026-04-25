
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
