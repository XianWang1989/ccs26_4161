
from django.contrib import admin
from django import forms
from .models import StuffModel  # Import your model

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formset, change):
        # Iterate through each form in the formset
        for obj in formset.save(commit=False):
            # Access the request object here
            obj.user = request.user  # Example usage with request.user
            obj.save()  # Save the instance

        formset.save_m2m()  # Save many-to-many relations if any

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainAdmin)  # Register your main model admin
