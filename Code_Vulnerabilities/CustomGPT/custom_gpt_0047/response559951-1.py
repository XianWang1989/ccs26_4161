
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel, MediaItem

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, change):
        super().save_related(request, form, change)
        # Access instance (the object being saved)
        obj = form.instance
        # Here you can update the object with the request user
        obj.user = request.user
        obj.save()

class MediaItemAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MediaItem, MediaItemAdmin)
