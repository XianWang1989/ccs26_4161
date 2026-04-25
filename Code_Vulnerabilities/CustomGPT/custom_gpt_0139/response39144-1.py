
from django.db import models

class CompanyProfile(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Custom save logic can be added here
        super(CompanyProfile, self).save(*args, **kwargs)
