
from django.db import models

class CompanyProfile(models.Model):
    # Your fields here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Add any custom pre-save logic here if needed
        super().save(*args, **kwargs)
