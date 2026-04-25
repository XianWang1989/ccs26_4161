
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StuffForm, self).save(commit=False)
        if self.request:
            instance.user = self.request.user  # Assign the user from request
        if commit:
            instance.save()
        return instance

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to the form
        return formset

class YourModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
