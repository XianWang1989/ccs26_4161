
from django.db import models

class CompanyProfile(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=100)
    established_date = models.DateField()

    def save(self, *args, **kwargs):
        # Additional logic before saving, if needed
        super(CompanyProfile, self).save(*args, **kwargs)
