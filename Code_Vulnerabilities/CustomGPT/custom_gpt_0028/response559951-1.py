
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from yourapp.models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Modify obj here
                obj.user = request.user  # Example modification
                obj.save()
