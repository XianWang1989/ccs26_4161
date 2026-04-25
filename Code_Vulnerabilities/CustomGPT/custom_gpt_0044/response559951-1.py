
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StuffForm, self).save(commit=False)
        if self.request:
            # Access request data, e.g., instance.user = self.request.user
            instance.user = self.request.user  # Example modification
        if commit:
            instance.save()
        return instance

class StuffAdmin(GenericStackedInline):
    model = StuffModel

    def get_formset(self, request, obj=None, **kwargs):
        # Get the formset based on the request
        formset = super().get_formset(request, obj, **kwargs)
        formset.form = lambda *args, **kwargs: StuffForm(*args, request=request, **kwargs)
        return formset
