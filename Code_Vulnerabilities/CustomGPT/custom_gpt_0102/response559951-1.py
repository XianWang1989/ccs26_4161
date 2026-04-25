
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.TabularInline):  # Use TabularInline or StackedInline based on your layout preference
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, formset, change):
        # Here we can access the request object
        instances = formset.save(commit=False)
        for obj in instances:
            # Modify the obj here as needed
            obj.user = request.user  # Example: assigning the user to the model
            obj.save()  # Save the modified instance
        formset.save_m2m()  # Save many-to-many relationships if needed

@admin.register(YourMainModel)  # Replace with your actual main model
class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
