
from django.contrib import admin
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

    def save(self, *args, **kwargs):
        # Custom logic if needed
        super().save(*args, **kwargs)

class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Add fields to display in admin

admin.site.register(CompanyProfile, CompanyProfileAdmin)
