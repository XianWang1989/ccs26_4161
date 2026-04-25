
from django.db import models

class CompanyProfile(models.Model):
    # Your fields here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Add any pre-save logic here if needed
        super().save(*args, **kwargs)
        # Add any post-save logic here if needed
