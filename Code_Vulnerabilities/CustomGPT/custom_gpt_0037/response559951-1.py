
from django.contrib import admin
from django import forms
from .models import StuffModel, ParentModel  # Adjust the imports to your actual models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffInline(admin.GenericStackedInline):  # or GenericTabularInline
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, change):
        # Access your object
        instances = form.save(commit=False)  # Save but not commit to DB yet
        for obj in instances:
            # Perform your custom logic here
            obj.user = request.user  # Set any fields based on the request
            obj.save()  # Now save to DB
        super().save_related(request, form, change)  # Call the parent method

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffInline]

admin.site.register(ParentModel, ParentModelAdmin)
