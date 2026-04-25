
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
        # This is where you can access the request object
        instances = formset.save(commit=False)

        # Loop through the instances and update them as necessary
        for instance in instances:
            # Perform operations using the request object
            instance.user = request.user  # Example of setting the user
            instance.save()  # Save the instance after modifications

        formset.save_m2m()  # Call to save many-to-many relationships, if any

# Register your admin classes
class YourModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

# Register your parent model
admin.site.register(YourParentModel, YourModelAdmin)
