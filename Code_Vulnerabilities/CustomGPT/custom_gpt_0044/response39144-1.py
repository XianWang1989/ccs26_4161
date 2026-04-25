
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as necessary

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Custom logic before saving, if any
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)

    def __str__(self):
        return self.name
