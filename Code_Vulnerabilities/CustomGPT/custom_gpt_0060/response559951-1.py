
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel  # Adjust the import according to your project structure

# Step 1: Create a custom form
class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust to include the fields you want

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Step 2: Get the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(StuffForm, self).save(commit=False)
        if self.request:
            obj.user = self.request.user  # Here you can access the request object
        if commit:
            obj.save()
        return obj

# Step 3: Use the custom form in your GenericStackedInline
class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    # Override the get_formset method to pass the request to the form
    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.form.request = request  # Attach the request to the formset
        return formset

# Assuming you have a main admin class for the parent model
class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)  # Register the parent model admin
