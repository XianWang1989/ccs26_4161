
from django.contrib import admin
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Add custom logic here if needed
        super().save(force_insert, force_update, *args, **kwargs)

# Register the model with Django admin
@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
