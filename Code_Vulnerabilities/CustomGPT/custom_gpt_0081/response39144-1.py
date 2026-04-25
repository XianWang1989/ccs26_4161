
from django.db import models

class CompanyProfile(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, force_insert=False, force_update=False, **kwargs):
        # Your custom saving logic (if any) can go here
        super(CompanyProfile, self).save(force_insert, force_update, **kwargs)

# Register your model in admin.py if you haven't done so
from django.contrib import admin

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
