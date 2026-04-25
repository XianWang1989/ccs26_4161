
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.request = request  # Store the request
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(StuffForm, self).save(commit=False)
        obj.user = self.request.user  # Use request to assign user
        if commit:
            obj.save()
        return obj

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to the form
        return formset
