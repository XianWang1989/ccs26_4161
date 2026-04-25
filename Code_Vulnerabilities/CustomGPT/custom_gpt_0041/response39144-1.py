
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # You can add any custom logic here before saving
        super(CompanyProfile, self).save(*args, **kwargs)

