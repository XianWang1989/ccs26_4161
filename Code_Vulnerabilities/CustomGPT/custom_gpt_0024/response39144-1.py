
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        # Add any pre-save logic here if needed
        super(CompanyProfile, self).save(*args, **kwargs)  # Correct call to super
        # Add any post-save logic here if needed
