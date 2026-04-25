
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel, YourMainModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def save(self, commit=True):
        # Access the request object if provided in kwargs.
        request = self._request
        obj = super().save(commit=False)
        if request:
            # Do something with the request object, e.g., set the user
            obj.user = request.user  # or any other field you want to update
        if commit:
            obj.save()
        return obj

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    # Overriding the get_formset method to pass the request to the form
    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request  # Attach request to the formset
        return formset

    # When initializing the Form, ensure to pass the request to it
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form._request = request  # Attach request to the form
        return form

class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, YourMainModelAdmin)
