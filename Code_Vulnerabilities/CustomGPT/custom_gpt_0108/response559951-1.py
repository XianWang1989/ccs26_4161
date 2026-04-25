
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel, ParentModel

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(StuffForm, self).save(commit=False)
        if self.request:
            # Access the request object and perform updates
            obj.user = self.request.user  # Example: setting the user
        if commit:
            obj.save()
        return obj

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to the form
        return formset

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)
