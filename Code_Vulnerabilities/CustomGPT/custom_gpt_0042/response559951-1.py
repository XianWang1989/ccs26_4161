
from django.contrib import admin
from django import forms
from .models import StuffModel, MediaItem

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, formset, change):
        # Iterate through the formset and access each instance
        instances = formset.save(commit=False)
        for obj in instances:
            # Access the request object here
            obj.user = request.user  # Example of setting a user field
            obj.save()
        formset.save_m2m()  # Save many-to-many relations

class MediaItemAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

    def save_model(self, request, obj, form, change):
        obj.save()  # Save the main model instance

admin.site.register(MediaItem, MediaItemAdmin)
