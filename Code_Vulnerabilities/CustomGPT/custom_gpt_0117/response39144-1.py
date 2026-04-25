
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Custom logic (if any) before saving
        super(CompanyProfile, self).save(*args, **kwargs)  # Ensure super is called correctly
