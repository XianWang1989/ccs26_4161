
from django.db import models

class CompanyProfile(models.Model):
    # Your fields here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Additional logic here if needed
        super(CompanyProfile, self).save(*args, **kwargs)
