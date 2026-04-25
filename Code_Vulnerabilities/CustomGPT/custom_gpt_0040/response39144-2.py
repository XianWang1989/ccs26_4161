
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Pre-save logic here
        super().save(*args, **kwargs)  # Simplified for Python 3
