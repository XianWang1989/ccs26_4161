
from django.urls import reverse  # Import reverse for URL lookup

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return reverse('api_v1_gallery_detail', kwargs={'pk': self.pk})  # Adjust according to your URL patterns
