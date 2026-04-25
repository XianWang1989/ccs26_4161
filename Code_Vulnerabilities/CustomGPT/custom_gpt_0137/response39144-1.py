
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    # Add other fields as necessary

    def save(self, *args, **kwargs):
        # You can add custom logic here, if needed
        super(CompanyProfile, self).save(*args, **kwargs)  # Correctly use super()
