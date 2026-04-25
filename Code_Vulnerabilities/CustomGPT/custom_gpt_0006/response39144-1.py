
from django.db import models

class CompanyProfile(models.Model):
    # Your model fields here
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # You can add custom logic here if needed
        super(CompanyProfile, self).save(*args, **kwargs)
