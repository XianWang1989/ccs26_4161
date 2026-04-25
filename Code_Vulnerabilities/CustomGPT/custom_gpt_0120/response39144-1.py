
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=255)
    # Other fields...

    def save(self, *args, **kwargs):
        # Add any custom save logic here if needed
        super().save(*args, **kwargs)  # Correct usage of super()
