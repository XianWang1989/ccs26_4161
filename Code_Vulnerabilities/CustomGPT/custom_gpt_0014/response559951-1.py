
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(StuffForm, self).save(commit=False)
        # Update obj with request data here
        if self.request:
            obj.user = self.request.user  # Example: set the user
        if commit:
            obj.save()
        return obj

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
