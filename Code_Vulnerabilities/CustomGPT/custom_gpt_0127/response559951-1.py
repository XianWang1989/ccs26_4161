
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get request if passed
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(commit=False)
        if self.request:
            obj.user = self.request.user  # Assign request user
        if commit:
            obj.save()
        return obj

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to form
        return formset

admin.site.register(YourModel, StuffAdmin)
