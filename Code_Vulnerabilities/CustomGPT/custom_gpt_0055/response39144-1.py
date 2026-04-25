
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=255)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Add any custom logic here, if needed
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
