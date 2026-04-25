
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    def save(self, commit=True):
        # Access the request object here using the cleaned data
        obj = super().save(commit=False)
        # You can access the request from the instance if passed during initialization
        request = self.request
        if request:
            obj.user = request.user  # Update your model as needed
        if commit:
            obj.save()
        return obj

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to the form
        return formset

admin.site.register(YourMainModel, YourMainModelAdmin)  # Register your main model admin
