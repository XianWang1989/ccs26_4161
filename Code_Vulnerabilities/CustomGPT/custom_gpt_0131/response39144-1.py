
from django.db import models

class CompanyProfile(models.Model):
    # Your model fields here
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Additional logic before saving if needed
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
