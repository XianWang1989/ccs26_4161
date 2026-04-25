
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

# Step 1: Create a custom form
class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StuffForm, self).save(commit=False)
        if self.request:  # Check if request is available
            instance.user = self.request.user  # Assign user from request
        if commit:
            instance.save()
        return instance

# Step 2: The admin inline class
class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        # Pass the request to the form
        formset = super().get_formset(request, obj, **kwargs)
        formset.form = lambda *args, **kwargs: self.form(**{**kwargs, 'request': request})
        return formset

# Step 3: Register your model and admin
@admin.register(YourModel)  # Replace with your actual model
class YourModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
