
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel  # Import your model

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Capture the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(StuffForm, self).save(commit=False)
        if self.request:
            # Set a field on your model using the request
            obj.user = self.request.user  # For example, assigning the logged-in user
        if commit:
            obj.save()
        return obj

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to the formset
        return formset

# Register your models with the admin class
class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, MainAdmin)  # Replace `YourMainModel` with your actual model
