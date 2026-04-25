
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

    def save_formset(self, request, form, formset, change):
        super().save_formset(request, form, formset, change)
        for obj in formset.save(commit=False):
            # Here you can modify the object before saving.
            obj.user = request.user  # Example to save the request user
            obj.save()

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

