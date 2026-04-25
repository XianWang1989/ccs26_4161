
# admin.py
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Capture the request object
        self.request = kwargs.pop('request', None)
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # You can access the request object here
        if self.request:
            # Here you can do the modification before saving
            self.instance.user = self.request.user  # Example of setting the user before saving
        return super(StuffForm, self).save(commit)

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        # Pass the request to the form
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.form.request = request  # Attach request to the form
        return formset

# Register the admin class with the model
class MyModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyModel, MyModelAdmin)
