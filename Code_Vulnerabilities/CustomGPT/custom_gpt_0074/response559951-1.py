
from django import forms
from django.contrib import admin
from .models import StuffModel  # Make sure to import your model

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Capture the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StuffForm, self).save(commit=False)
        if self.request:  # Check if request is available
            instance.user = self.request.user  # Set the user before saving
        if commit:
            instance.save()
        return instance

class StuffAdmin(admin.GenericStackedInline):  # Changed to use GenericStackedInline
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass request object to the formset forms
        return formset

class MyModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]  # Include the inline in your main admin

admin.site.register(MyModel, MyModelAdmin)  # Register your main model admin
