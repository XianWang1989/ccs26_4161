
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # add other fields here

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Custom logic can go here (if needed)
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
