
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # You can add custom logic here
        super(CompanyProfile, self).save(*args, **kwargs)
