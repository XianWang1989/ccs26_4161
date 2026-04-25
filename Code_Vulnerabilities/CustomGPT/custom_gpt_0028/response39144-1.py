
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def save(self, *args, **kwargs):
        # Add any custom logic here, if necessary
        super(CompanyProfile, self).save(*args, **kwargs)
