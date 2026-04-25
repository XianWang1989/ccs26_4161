
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust according to your fields

class StuffFormSet(forms.BaseModelFormSet):
    def save(self, commit=True):
        for form in self.forms:
            if form.cleaned_data:  # Check if the form is valid and has data
                obj = form.save(commit=False)
                # Access the request here if necessary
                obj.save()
        if commit:
            self.save_m2m()  # Save many-to-many relationships if applicable

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm
    formset = StuffFormSet

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request  # Attach the request to the formset
        return formset
