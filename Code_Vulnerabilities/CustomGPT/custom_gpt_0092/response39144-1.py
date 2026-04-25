
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # Other fields here

    def save(self, *args, **kwargs):
        # Custom logic before saving if needed
        super(CompanyProfile, self).save(*args, **kwargs)
        # Custom logic after saving if needed
