
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Custom logic before saving
        super().save(*args, **kwargs)  # Call the superclass method
        # Custom logic after saving
