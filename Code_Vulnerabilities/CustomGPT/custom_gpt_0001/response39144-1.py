
from django.db import models

class CompanyProfile(models.Model):
    # Your fields go here, e.g.
    name = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, force_insert=False, force_update=False, **kwargs):
        # Any custom save logic can go here
        super(CompanyProfile, self).save(force_insert, force_update, **kwargs)
