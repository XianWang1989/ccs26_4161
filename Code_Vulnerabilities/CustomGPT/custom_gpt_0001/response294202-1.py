
from django.db import models
from django.urls import reverse

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_via_uri(self):
        return reverse('api_dispatch_detail', args=[self._meta.app_label, 'gallery', self.id])


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
