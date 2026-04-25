
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        from tastypie.api import Api
        return Api().urls['/api/v1/gallery/%s/' % self.id]
