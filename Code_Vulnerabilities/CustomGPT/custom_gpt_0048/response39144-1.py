
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Other fields...

    def save(self, *args, **kwargs):
        # Any custom logic before saving can go here
        super(CompanyProfile, self).save(*args, **kwargs)
