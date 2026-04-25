
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

    def save(self, *args, **kwargs):
        # Any custom logic here
        super(CompanyProfile, self).save(*args, **kwargs)  # Correct usage of super()
