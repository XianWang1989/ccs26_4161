
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        # Access the formset and iterate through the instances
        instances = formset.save(commit=False)
        for obj in instances:
            obj.user = request.user  # Set the user or any other field
            obj.save()  # Save the object

        formset.save_m2m()  # Save many-to-many relationships

# Register your admin model
class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)
