
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel, ParentModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, formset, change):
        instances = formset.save(commit=False)
        for obj in instances:
            # Here you can access the request object
            obj.user = request.user  # Example of setting user before saving
            obj.save()
        formset.save_m2m()  # Save many-to-many relationships, if applicable

class ParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentAdmin)
