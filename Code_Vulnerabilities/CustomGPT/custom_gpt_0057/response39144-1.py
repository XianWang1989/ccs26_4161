
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        print("Saving CompanyProfile: ", self.name)
        super().save(force_insert, force_update, *args, **kwargs)
