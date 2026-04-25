
from django.contrib import admin
from django import forms
from .models import StuffModel, ParentModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formset, change):
        super().save_related(request, form, formset, change)  # Call parent method to ensure proper save
        for obj in formset.save(commit=False):
            # Access the request object and modify the model instance
            obj.user = request.user  # Example: set user before saving
            obj.save()

@admin.register(ParentModel)
class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
