
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # Other fields...

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Perform any custom logic before saving
        super().save(force_insert, force_update, *args, **kwargs)
