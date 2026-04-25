
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Ensure you call the parent save method correctly
        super(CompanyProfile, self).save(*args, **kwargs)
