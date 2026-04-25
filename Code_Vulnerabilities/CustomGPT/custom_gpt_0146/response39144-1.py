
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    # Add any other fields you need here

    def save(self, *args, **kwargs):
        # Add any custom logic here if needed
        super(CompanyProfile, self).save(*args, **kwargs)
