
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('api_dispatch_list', kwargs={'resource_name': 'gallery'})
