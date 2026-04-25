
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)
    # Add more fields as needed

    def save(self, *args, **kwargs):
        # Perform any custom logic before saving if needed
        super(CompanyProfile, self).save(*args, **kwargs)
