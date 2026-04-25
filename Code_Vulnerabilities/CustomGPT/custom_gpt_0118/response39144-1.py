
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Additional logic can go here if needed
        super(CompanyProfile, self).save(*args, **kwargs)

