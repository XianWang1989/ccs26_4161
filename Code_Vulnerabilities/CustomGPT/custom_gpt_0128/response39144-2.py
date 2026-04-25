
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Add any custom pre-save logic here
        super().save(*args, **kwargs)  # Preferred syntax for Python 3
