
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel  # Adjust the import based on your models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for obj in instances:
            # Set attributes based on the request object before saving
            obj.user = request.user  # Example of using the request object
            obj.save()

        formset.save_m2m()  # Save many-to-many relationships if applicable
