
from django.contrib import admin
from django import forms
from .models import StuffModel  # Make sure to adjust the import based on your project structure

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formset, change):
        super().save_related(request, form, formset, change)

        # Accessing each object in the formset
        for obj in formset.save(commit=False):
            # Set user or any other field before saving
            obj.user = request.user
            obj.save()

@admin.register(YourParentModel)
class YourParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
