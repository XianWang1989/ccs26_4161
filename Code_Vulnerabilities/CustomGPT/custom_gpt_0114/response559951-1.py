
from django.contrib import admin
from django import forms
from .models import StuffModel  # Adjust according to your models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust fields as needed

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        # Access the object and update it
        if form.instance.pk:  # Ensure the object is being updated
            form.instance.user = request.user  # Set user or any other field
            form.instance.save()  # Save instance

# Use StuffAdmin in your main admin class
class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, MainAdmin)  # Replace with your main model
