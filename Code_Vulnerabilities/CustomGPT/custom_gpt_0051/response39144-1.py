
from django.db import models

class CompanyProfile(models.Model):
    # Your fields here
    name = models.CharField(max_length=255)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Your custom logic (if any) can go here
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
