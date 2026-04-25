
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from django.forms.models import BaseInlineFormSet
from .models import StuffModel  # Update this with your actual model import

class StuffInlineFormSet(BaseInlineFormSet):
    def __init__(self, request=None, *args, **kwargs):
        self.request = request  # Store the request object
        super().__init__(*args, **kwargs)

    def save_existing(self, commit=True):
        for form in self.forms:
            if form.instance.pk:  # Check for existing instance
                obj = form.save(commit=False)
                # Here you can modify the object before saving
                obj.user = self.request.user  # Example of using the request object
                if commit:
                    obj.save()

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    formset = StuffInlineFormSet

    def get_formset(self, request, obj=None, **kwargs):
        self.request = request  # Pass the request object
        return super().get_formset(request, obj, **kwargs)

# Register your admin class
class MyModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyModel, MyModelAdmin)  # Ensure you register your main model here
