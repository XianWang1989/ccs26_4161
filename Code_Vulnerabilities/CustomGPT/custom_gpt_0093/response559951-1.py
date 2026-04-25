
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Access the request object
        if hasattr(self, 'request'):
            instance.user = self.request.user  # Example: set user before saving
        if commit:
            instance.save()
        return instance

class StuffAdmin(GenericStackedInline):
    model = StuffModel

    def get_formset(self, request, obj=None, **kwargs):
        # Pass the request to the form
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Attach request to each form
        return formset

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user  # Example: set user before saving
            instance.save()
        formset.save_m2m()  # Save many-to-many relationships if needed

class StuffModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(StuffModel, StuffModelAdmin)
