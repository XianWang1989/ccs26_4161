
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Any custom save logic can be included here
        super(CompanyProfile, self).save(*args, **kwargs)
