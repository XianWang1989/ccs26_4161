
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        # Access the inline instance here before saving
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Modify the object as needed
                obj.user = request.user  # Assuming you want to set the user
                obj.save()  # Save the object

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
