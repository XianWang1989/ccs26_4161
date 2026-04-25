
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel  # Adjust your import according to your models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        # Loop through each form in the formset
        for obj in formset.save(commit=False):
            # Modify the object before saving
            obj.user = request.user  # Example of using the request object
            obj.save()
        formset.save_m2m()  # Save many-to-many relationships if any

@admin.register(YourMainModel)  # Register your main model
class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
