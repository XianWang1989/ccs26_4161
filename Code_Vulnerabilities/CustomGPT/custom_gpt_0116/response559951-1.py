
from django.contrib import admin
from django import forms
from .models import StuffModel  # Adjust the import based on your app structure

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust fields as necessary

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, formset, change):
        # Iterate through the objects in the formset
        for obj in formset.object_list:
            # Access the request object and modify the object before saving
            obj.user = request.user  # Example of setting a user field
            obj.save()  # Save the object

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, MainAdmin)  # Replace with your main model
