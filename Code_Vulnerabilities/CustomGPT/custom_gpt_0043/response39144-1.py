
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # You can include any custom logic here before saving
        super(CompanyProfile, self).save(*args, **kwargs)
