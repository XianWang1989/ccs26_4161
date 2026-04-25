
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
        # Access the instance and modify it
        instance = form.instance
        instance.user = request.user  # Example: setting a user field
        instance.save()

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainAdmin)
