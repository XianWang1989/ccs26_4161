
from django.db import models

class CompanyProfile(models.Model):
    # Your model fields here
    name = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Optional additional logic before saving
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
