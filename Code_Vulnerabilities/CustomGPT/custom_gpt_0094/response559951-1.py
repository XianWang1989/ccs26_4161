
from django.contrib import admin
from django import forms
from .models import StuffModel  # Adjust as necessary

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Include all fields or specify

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        # Here you can now access the request object
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Do your custom logic before saving
                obj.user = request.user  # Example: setting the user
                obj.save()

@admin.register(YourMainModel)  # Replace with your main model
class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

