
from django.db import models

class CompanyProfile(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, **kwargs):
        # Perform any custom logic here
        super(CompanyProfile, self).save(force_insert, force_update, **kwargs)

