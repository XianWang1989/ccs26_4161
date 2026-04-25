
from django.contrib import admin
from django import forms
from .models import StuffModel  # Make sure to import your model

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.TabularInline):  # or use GenericStackedInline accordingly
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formset, change):
        # Iterate through the instances in the formset
        for obj in formset.save(commit=False):
            # You can access the request here and modify the obj
            obj.user = request.user  # Example: set the user before saving
            obj.save()
        formset.save_m2m()  # Save many-to-many relationships, if any

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

# Register the main admin class
admin.site.register(MainModel, MainAdmin)  # Replace MainModel with your main model
