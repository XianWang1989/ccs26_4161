
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=255)
    # Other fields...

    def save(self, *args, **kwargs):
        # Custom logic before saving
        super(CompanyProfile, self).save(*args, **kwargs)
