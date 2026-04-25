
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from django.forms.models import BaseInlineFormSet
from .models import StuffModel

# Step 1: Create a custom formset
class StuffInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract the request
        super(StuffInlineFormSet, self).__init__(*args, **kwargs)

    def save_new(self, instance, commit=True):
        # Use self.request here if needed
        instance.user = self.request.user  # Example of using request.user
        super().save_new(instance, commit=commit)

# Step 2: Create a custom inline
class StuffAdmin(GenericStackedInline):
    model = StuffModel
    formset = StuffInlineFormSet

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request  # Pass the request to the formset
        return formset

# Step 3: Register your admin
class MyAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyModel, MyAdmin)
