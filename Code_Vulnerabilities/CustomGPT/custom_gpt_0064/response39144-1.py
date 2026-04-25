
from django.db import models

class CompanyProfile(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Custom save logic (if any)
        super().save(force_insert, force_update, *args, **kwargs)  # Use super() without arguments
