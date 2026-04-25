
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StuffForm, self).save(commit=False)
        # Access the request object here
        if self.request:
            instance.user = self.request.user  # Assign the user before saving
        if commit:
            instance.save()
        return instance

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.request = request  # Pass the request to the formset
        return formset

    def get_form(self, request, obj=None, **kwargs):
        form = super(StuffAdmin, self).get_form(request, obj, **kwargs)
        form.request = request  # Pass the request to the form
        return form
