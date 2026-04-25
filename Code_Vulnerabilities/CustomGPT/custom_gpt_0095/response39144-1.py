
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Call the original save method
        super(CompanyProfile, self).save(*args, **kwargs)
