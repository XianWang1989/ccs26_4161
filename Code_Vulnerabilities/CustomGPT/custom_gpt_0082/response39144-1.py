
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # You can perform additional logic here before saving
        super(CompanyProfile, self).save(*args, **kwargs)
