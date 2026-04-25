
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def save(self, commit=True):
        obj = super().save(commit=False)
        # Access the request here if needed
        if commit:
            obj.save()
        return obj

class StuffInline(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Store request in the formset
        return formset

class StuffAdmin(admin.ModelAdmin):
    inlines = [StuffInline]
