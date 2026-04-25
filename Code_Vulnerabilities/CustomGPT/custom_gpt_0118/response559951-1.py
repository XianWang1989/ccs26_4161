
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

    def save_related(self, request, formset, change):
        super().save_related(request, formset, change)
        for obj in formset.save(commit=False):
            # Access the request object here
            obj.user = request.user  # Example of setting the user
            obj.save()

class MainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

# Register your models
admin.site.register(MainModel, MainModelAdmin)
