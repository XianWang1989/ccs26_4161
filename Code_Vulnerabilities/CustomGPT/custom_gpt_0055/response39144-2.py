
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Custom logic can go here
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
