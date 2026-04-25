
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')  # added related_name for better querying
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
