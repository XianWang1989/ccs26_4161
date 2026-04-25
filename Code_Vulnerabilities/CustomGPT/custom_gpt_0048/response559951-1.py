
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffInline(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        # Access the instance and modify it before saving
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Set user or any other attribute before saving
                obj.user = request.user  # Assuming you have a user field
                obj.save()

class StuffAdmin(admin.ModelAdmin):
    inlines = [StuffInline]

admin.site.register(YourMainModel, StuffAdmin)
