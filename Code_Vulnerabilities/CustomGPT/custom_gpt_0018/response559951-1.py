
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

class YourMainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

    def save_related(self, request, form, formsets, change):
        # This is where you have access to the request object
        super().save_related(request, form, formsets, change)

        for formset in formsets:
            # Loop through the forms in the formset
            for obj in formset.save(commit=False):
                # Here you can assign request.user or other properties
                obj.user = request.user  # Example: setting user to the instance
                obj.save()  # Now save the instance

# Register your main admin class
admin.site.register(YourMainModel, YourMainAdmin)
