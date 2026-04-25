
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Add any custom save logic here if needed
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
