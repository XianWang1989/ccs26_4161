
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return '/api/v1/gallery/%s/' % self.id  # Adjust this to your URL structure
