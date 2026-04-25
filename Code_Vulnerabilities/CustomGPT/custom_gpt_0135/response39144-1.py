
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields here

    def save(self, *args, **kwargs):
        # Custom save operations can go here

        # Call the parent class's save method
        super(CompanyProfile, self).save(*args, **kwargs)

