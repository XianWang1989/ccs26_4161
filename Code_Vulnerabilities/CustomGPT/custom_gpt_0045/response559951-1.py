
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel, ParentModel  # Adjust the import based on your actual models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, formset, change):
        # Here you can access the request object
        instances = formset.save(commit=False)
        for obj in instances:
            # Update the object with request data if necessary
            obj.user = request.user  # or any other field you want to set
            obj.save()
        formset.save_m2m()  # If you have ManyToMany relationships

class ParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

# Register the parent model admin
admin.site.register(ParentModel, ParentAdmin)
