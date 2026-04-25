
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        # Access the request object here
        instances = formset.save(commit=False)
        for obj in instances:
            # You can set the user or any other request property
            obj.user = request.user  # Assuming `user` is a field in StuffModel
            obj.save()  # Save the instance
        formset.save_m2m()  # Save any many-to-many relationships if necessary

# Register your models with the custom admin class
