
from django.contrib import admin
from django import forms
from .models import StuffModel, MediaItem  # Adjust the import according to your models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        # Loop through all the formsets to access the instances
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Here you can modify the object before saving
                obj.user = request.user  # Example of assigning user
                obj.save()
            formset.save_m2m()  # Save any many-to-many relationships

class MediaItemAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MediaItem, MediaItemAdmin)
