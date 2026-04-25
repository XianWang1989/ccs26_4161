
from django.db import models

class CompanyProfile(models.Model):
    # Your model fields go here

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Add any custom logic here if needed
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
