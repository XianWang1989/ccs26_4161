
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        # Construct and return the URI for the gallery
        return "/api/v1/gallery/%d/" % self.id
