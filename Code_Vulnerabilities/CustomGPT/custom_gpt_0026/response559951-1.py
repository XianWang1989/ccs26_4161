
from django.contrib import admin
from django import forms
from .models import StuffModel, ParentModel  # Adjust import based on your models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Perform your modifications before saving
                obj.user = request.user  # Example: setting user
                obj.save()

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)
