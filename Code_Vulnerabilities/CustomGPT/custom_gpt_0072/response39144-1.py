
from django.db import models

class CompanyProfile(models.Model):
    # Your fields here
    name = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Your custom save logic here, if any
        super(CompanyProfile, self).save(force_insert=force_insert, force_update=force_update, *args, **kwargs)
