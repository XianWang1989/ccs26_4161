
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel  # Replace with your actual model

# Custom Form
class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get the request if available
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # Access the request object and perform actions before saving
        if self.request:
            # Example: setting a user based on request
            self.instance.user = self.request.user

        return super(StuffForm, self).save(commit=commit)

# Admin Inline
class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to the form
        return formset

# Register your admin
class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, MainAdmin)  # Replace with your actual main model
