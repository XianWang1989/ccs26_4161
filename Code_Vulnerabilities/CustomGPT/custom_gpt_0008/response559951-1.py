
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Capture the request
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # Access the request object here
        obj = super(StuffForm, self).save(commit=False)
        if self.request:
            obj.user = self.request.user  # Example: Set obj.user to the current user
        if commit:
            obj.save()
        return obj

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.form = self.form  # Set the custom form
        return formset

    def get_form(self, request, obj=None, **kwargs):
        form = super(StuffAdmin, self).get_form(request, obj, **kwargs)
        form.request = request  # Pass the request to the form
        return form

@admin.register(YourMainModel)
class YourMainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]  # Add your inline admin here
