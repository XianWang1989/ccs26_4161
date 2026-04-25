
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as necessary

    def save(self, *args, **kwargs):
        # Custom logic here, if any
        super().save(*args, **kwargs)  # Corrected super usage
