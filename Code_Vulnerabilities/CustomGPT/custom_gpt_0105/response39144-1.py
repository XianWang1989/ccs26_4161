
from django.db import models

class CompanyProfile(models.Model):
    # Your fields go here

    def save(self, force_insert=False, force_update=False, **kwargs):
        # Your custom logic here (if any)
        super().save(force_insert, force_update, **kwargs)
