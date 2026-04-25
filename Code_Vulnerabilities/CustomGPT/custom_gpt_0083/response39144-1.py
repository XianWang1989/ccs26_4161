
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as needed

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # You can add custom logic here
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
