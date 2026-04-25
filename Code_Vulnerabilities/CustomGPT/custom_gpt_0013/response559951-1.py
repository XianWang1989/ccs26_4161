
from django.contrib import admin
from django import forms
from .models import StuffModel
from django.contrib.contenttypes.admin import GenericStackedInline

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formset, change):
        # Iterate through the formset to get the model instances
        for obj in formset.save(commit=False):
            # Access the request object here and update the instance
            obj.user = request.user  # Example: set the user before saving
            obj.save()  # Now save the instance

# Register your admin class
class MyModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyModel, MyModelAdmin)
