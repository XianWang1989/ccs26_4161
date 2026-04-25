
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def save(self, commit=True):
        # Access the request object here
        request = self.request  # Use self.request to get it from the form
        obj = super().save(commit=False)
        obj.user = request.user  # Set user before save
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

# Register your models
@admin.register(ParentModel)
class ParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
