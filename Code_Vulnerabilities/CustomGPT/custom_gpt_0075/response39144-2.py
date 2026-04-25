
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Perform any custom actions before saving
        super().save(*args, **kwargs)  # Call the parent class's save method
