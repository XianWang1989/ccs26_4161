
from django.contrib import admin
from django import forms
from .models import StuffModel  # Make sure to import your model

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust fields as needed

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        # Access the queryset and iterate through each form in the formset
        instances = formset.save(commit=False)
        for obj in instances:
            obj.user = request.user  # Assign request.user or any other modifications
            obj.save()
        formset.save_m2m()  # Save many-to-many relationships, if any

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, MainAdmin)  # Register your main model
