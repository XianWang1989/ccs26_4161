
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Add your other fields here

    def save(self, *args, **kwargs):
        # You may perform any custom logic here before saving
        super(CompanyProfile, self).save(*args, **kwargs)
