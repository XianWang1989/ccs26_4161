
from django.urls import reverse

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('api_dispatch_detail', args=[self.pk])
