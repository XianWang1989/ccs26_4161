
from django.contrib import admin
from django import forms
from .models import StuffModel, YourMainModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)  # Call the original implementation
        # Access the items in the formset to modify them
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Here you can access the request and set the user or any other attribute
                obj.user = request.user  # Example: setting user attribute
                obj.save()  # Save the object

class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, YourMainModelAdmin)
