
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formset, change):
        # Loop through objects in the formset and set the user
        for obj in formset.save(commit=False):
            obj.user = request.user  # Assign the current user
            obj.save()
        formset.save_m2m()  # Save many-to-many relationships if necessary

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)
