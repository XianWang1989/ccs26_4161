
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # Here, you can access self.request and use it
        instance = super(StuffForm, self).save(commit=False)
        if self.request:
            instance.user = self.request.user  # Or any other logic with request
        if commit:
            instance.save()
        return instance

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Passing the request to the form
        return formset

admin.site.register(YourMainModel, YourMainModelAdmin)
