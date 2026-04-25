
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

# Custom form to handle the saving of the model
class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract request from kwargs
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StuffForm, self).save(commit=False)
        if self.request:
            # Here you can modify the instance using self.request
            instance.user = self.request.user  # or any other modification
        if commit:
            instance.save()
        return instance

# GenericStackedInline class
class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    # Override get_formset to pass the request
    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to the form
        return formset

# Register your admin classes
class ItemAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ItemModel, ItemAdmin)
