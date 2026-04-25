
# models.py
from django.db import models
from .utils import post_content  # Import the post_content function from utils

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(self)  # Call the function directly with self
        super(Shastra, self).save(*args, **kwargs)

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)
