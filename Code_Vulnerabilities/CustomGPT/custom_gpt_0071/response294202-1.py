
from django.urls import reverse

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def get_via_uri(self):
        return reverse('api_dispatch_detail', args=['v1', 'gallery', self.id])
