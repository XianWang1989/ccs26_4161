
from django.contrib import admin
from django import forms
from your_app.models import StuffModel, MainModel  # Replace with your actual models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        # Loop through each form in the formset
        instances = formset.save(commit=False)
        for obj in instances:
            # Access the request object
            obj.user = request.user  # Assuming you want to set the user
            obj.save()  # Now you can call save() on the object
        formset.save_m2m()  # Save many-to-many relationships after saving instances

class MainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainModelAdmin)
