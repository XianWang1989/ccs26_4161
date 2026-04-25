
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # Custom logic here (if needed)

        super(CompanyProfile, self).save(force_insert, force_update, using, update_fields)
