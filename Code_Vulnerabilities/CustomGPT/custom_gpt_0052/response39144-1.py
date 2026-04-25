
from django.db import models

class CompanyProfile(models.Model):
    # Your model fields here
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Custom logic before saving can go here
        super(CompanyProfile, self).save(*args, **kwargs)
