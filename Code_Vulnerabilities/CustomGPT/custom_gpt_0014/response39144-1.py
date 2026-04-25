
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=255)
    # Add other fields as needed

    def save(self, *args, **kwargs):
        # Custom logic before saving, if needed
        super().save(*args, **kwargs)  # Correctly call the superclass method
