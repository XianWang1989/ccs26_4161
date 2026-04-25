
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def save(self, *args, **kwargs):
        # Add any custom logic here if needed
        super(CompanyProfile, self).save(*args, **kwargs)

