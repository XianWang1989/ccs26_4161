
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Custom logic can be placed here
        super(CompanyProfile, self).save(*args, **kwargs)
