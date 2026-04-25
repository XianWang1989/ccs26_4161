
from django import forms
from django.contrib import admin
from django.contrib.admin import StackedInline
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel  # Adjust the import according to your project structure

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save_new(self, instance, commit=True):
        # Here you have access to the request
        instance.user = self.request.user  # Example of using the request user
        super().save_new(instance, commit)

    def save_existing(self, instance, commit=True):
        # Here you can also access the request
        instance.user = self.request.user  # Example of updating the user
        super().save_existing(instance, commit)

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request  # Pass the request to the formset
        return formset

@admin.register(YourMainModel)  # Replace with your actual model
class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
