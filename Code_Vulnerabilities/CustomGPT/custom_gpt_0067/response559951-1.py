
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
        super().save_related(request, form, formset, change)
        # Modify the instance here
        for obj in formset.save(commit=False):
            obj.user = request.user  # Set the user or any other attribute
            obj.save()

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, MainAdmin)
