
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')  # Add related_name here
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
