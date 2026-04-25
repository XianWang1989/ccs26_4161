
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Any custom logic before saving
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
