
from django.contrib import admin
from django import forms
from django.forms.models import BaseInlineFormSet
from .models import StuffModel, ParentModel

# Create a custom formset to access the request object
class StuffInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(StuffInlineFormSet, self).__init__(*args, **kwargs)

    def save_new(self, form, commit=True):
        # Here you can access self.request
        obj = super(StuffInlineFormSet, self).save_new(form, commit)
        if self.request:
            # example logic, e.g. obj.user = self.request.user
            obj.user = self.request.user
            obj.save()
        return obj

    def save_existing(self, form, commit=True):
        obj = super(StuffInlineFormSet, self).save_existing(form, commit)
        if self.request:
            # Handle updates if necessary
            obj.user = self.request.user
            obj.save()
        return obj

class StuffAdmin(admin.TabularInline):
    model = StuffModel
    formset = StuffInlineFormSet

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

    def get_formset(self, request, *args, **kwargs):
        formset = super(ParentModelAdmin, self).get_formset(request, *args, **kwargs)
        formset.request = request  # passing request to formset
        return formset

admin.site.register(ParentModel, ParentModelAdmin)
