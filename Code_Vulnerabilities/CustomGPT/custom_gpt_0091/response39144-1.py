
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # You can add custom logic here if needed
        super(CompanyProfile, self).save(*args, **kwargs)  # Make sure you pass args and kwargs
