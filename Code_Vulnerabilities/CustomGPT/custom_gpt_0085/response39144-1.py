
from django.db import models

class CompanyProfile(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Perform any custom actions before saving
        super(CompanyProfile, self).save(*args, **kwargs)  # Correctly calls the parent class save method
