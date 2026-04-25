
from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name  # Use __str__ for Python 3

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
