
from django.db import models

class CompanyProfile(models.Model):
    # define your fields here
    name = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Add any custom behavior here if needed
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
