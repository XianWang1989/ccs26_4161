
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        # Iterate over each form in the formset
        instances = formset.save(commit=False)
        for obj in instances:
            # Access the request object and perform necessary operations
            obj.user = request.user  # Example: associate the current user
            obj.save()  # Save the model instance
        formset.save_m2m()  # Save many-to-many relations

# Register your admin class
class MyModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyModel, MyModelAdmin)
