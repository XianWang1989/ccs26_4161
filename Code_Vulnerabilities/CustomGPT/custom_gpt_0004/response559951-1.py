
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel, YourMainModel  # Adjust these imports based on your models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extracting the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(StuffForm, self).save(commit=False)
        if self.request:  # Ensure request is available
            obj.user = self.request.user  # Assign user or any required logic
        if commit:
            obj.save()
        return obj

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to each form
        return formset

class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, YourMainModelAdmin)
