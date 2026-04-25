
from django.contrib import admin
from django import forms
from .models import StuffModel, ParentModel  # Assuming you have these models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Include all fields, or specify your fields

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        # Capture the request object by updating kwargs
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request  # Store the request object for later use
        return formset

    def save_formset(self, request, formset, change):
        # Loop through the forms and save each one
        for form in formset:
            if form.cleaned_data:
                instance = form.save(commit=False)
                # Now you can modify the instance using request.user or other request attributes
                instance.user = request.user  # Example of setting the user
                instance.save()  # Save the instance

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)
