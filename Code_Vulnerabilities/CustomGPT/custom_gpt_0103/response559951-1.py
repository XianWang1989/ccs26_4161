
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Capture the request
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(StuffForm, self).save(commit=False)
        if self.request:
            # Example: set the user from the request
            obj.user = self.request.user
        if commit:
            obj.save()
        return obj

class StuffAdmin(admin.TabularInline):  # or GenericStackedInline
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to the form
        return formset

class BaseAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
