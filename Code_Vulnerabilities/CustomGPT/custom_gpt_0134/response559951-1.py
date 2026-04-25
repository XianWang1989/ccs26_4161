
from django.contrib import admin
from django import forms
from django.forms import models as formset_models
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffFormSet(formset_models.BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instances = super().save(commit=False)
        for instance in instances:
            if self.request:
                # Here, you can access the request and modify your instance
                instance.user = self.request.user
            if commit:
                instance.save()
        return instances

class StuffAdmin(admin.StackedInline):
    model = StuffModel
    formset = StuffFormSet

    def get_formset(self, request, *args, **kwargs):
        formset = super().get_formset(request, *args, **kwargs)
        formset.request = request  # Attach the request to the formset
        return formset

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, MainAdmin)
