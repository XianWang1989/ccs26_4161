
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Your custom logic before saving
        print("Saving the CompanyProfile instance")
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)
        # Your custom logic after saving
