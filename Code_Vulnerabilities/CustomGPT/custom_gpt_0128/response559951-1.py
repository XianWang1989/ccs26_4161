
from django.contrib import admin
from django import forms
from .models import StuffModel  # Adjust according to your model's location

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Specify your model fields here

class StuffAdmin(admin.TabularInline):  # Use StackedInline or TabularInline as needed
    model = StuffModel
    form = StuffForm

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        # Update instances from inline forms
        for formset in formsets:
            if isinstance(formset, StuffAdmin):  # Check if it's your inline
                for obj in formset.save(commit=False):  # Get unsaved instances
                    obj.user = request.user  # Set the user or any request-related data
                    obj.save()  # Save the instance

admin.site.register(MainModel, MainAdmin)  # Register your main model
