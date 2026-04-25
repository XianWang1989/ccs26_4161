
from django.contrib import admin
from django import forms
from .models import StuffModel, MainModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        # Access the request object here
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Modify the object before saving
                obj.user = request.user  # For example, set a user attribute
                obj.save()
            formset.save_m2m()  # Save many-to-many fields

class MainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainModelAdmin)
