
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_via_uri(self):
        from tastypie.api import Api
        api = Api(api_name='v1')
        return api.get_resource_uri(self)
