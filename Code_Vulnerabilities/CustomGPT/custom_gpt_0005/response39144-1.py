
from django.db import models

class CompanyProfile(models.Model):
    # Your model fields go here
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super(CompanyProfile, self).save(*args, **kwargs)
