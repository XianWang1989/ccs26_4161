
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)
    # Other fields...

    def save(self, *args, **kwargs):
        # Custom save logic (if any)
        super().save(*args, **kwargs)
