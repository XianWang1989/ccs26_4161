
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Any custom logic can go here
        super(CompanyProfile, self).save(*args, **kwargs)
