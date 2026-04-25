
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def save(self, commit=True):
        # Access the request via the instance's data
        if hasattr(self, 'request'):
            self.instance.user = self.request.user  # Example of setting user
        return super().save(commit=commit)

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        # Attach the request to the formset
        formset.request = request
        return formset

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Attach the request to the form
        form.request = request
        return form
