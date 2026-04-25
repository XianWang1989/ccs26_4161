
from django.db import models

class CompanyProfile(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=100)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Here you can add custom behavior before saving
        # For example, you might validate data or set default values
        super().save(*args, **kwargs)  # This calls the save method of the parent class
