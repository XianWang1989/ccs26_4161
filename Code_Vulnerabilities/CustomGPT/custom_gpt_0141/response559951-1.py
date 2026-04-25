
# admin.py
from django.contrib import admin
from django import forms
from yourapp.models import StuffModel  # Replace with your actual model

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust fields as needed

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(StuffForm, self).save(commit=False)
        if self.request:  # Modify the object using the request
            obj.user = self.request.user  # Example of setting the user
        if commit:
            obj.save()
        return obj

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to the form
        return formset

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainAdmin)  # Replace with your main model registration
