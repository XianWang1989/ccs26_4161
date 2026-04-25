
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
        # Iterate through the formsets and update the instance
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Here you can access the request
                obj.user = request.user  # Set the user or any other attribute
                obj.save()
        super().save_related(request, form, formsets, change)

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, MainAdmin)
