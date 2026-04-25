
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel, ParentModel  # Adjust import based on your models

# Custom form for your model
class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Capture the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(StuffForm, self).save(commit=False)
        if self.request:
            obj.user = self.request.user  # Set user from request
        if commit:
            obj.save()
        return obj

# Inline admin with custom form
class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        # Pass the request to the form
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.form.request = request  # Attach request to the formset form
        return formset

# Admin for the parent model
class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)
