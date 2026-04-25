
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

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        # Here you can access the request object
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Modify your object here
                obj.user = request.user  # Example: setting user before saving
                obj.save()

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainAdmin)
