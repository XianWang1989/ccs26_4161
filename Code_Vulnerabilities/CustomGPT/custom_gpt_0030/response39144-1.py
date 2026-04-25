
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Add custom logic here if needed

        # Call the parent's save method
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
