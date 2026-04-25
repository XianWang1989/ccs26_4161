
from django.contrib import admin
from django import forms
from .models import StuffModel, MediaItem

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffInline(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, formset, change):
        super().save_related(request, formset, change)

        # Here we can access the request object
        for obj in formset.save(commit=False):
            # Update the instance before saving
            obj.user = request.user  # e.g., setting the user
            obj.save()

class MediaItemAdmin(admin.ModelAdmin):
    inlines = [StuffInline]

admin.site.register(MediaItem, MediaItemAdmin)
