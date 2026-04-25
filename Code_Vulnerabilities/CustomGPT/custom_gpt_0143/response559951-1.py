
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust according to your fields

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        # Access the formset and iterate through forms
        instances = formset.save(commit=False)
        for obj in instances:
            # Update your instance here
            obj.user = request.user  # Example of assigning request user
            obj.save()
        formset.save_m2m()  # Save many-to-many relationships

class MainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainModelAdmin)
