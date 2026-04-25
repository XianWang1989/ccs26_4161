
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Add any custom logic here if needed
        super(CompanyProfile, self).save(*args, **kwargs)  # pass args and kwargs to super
