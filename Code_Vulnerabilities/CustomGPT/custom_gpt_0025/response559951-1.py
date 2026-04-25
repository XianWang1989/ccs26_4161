
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

    def save_related(self, request, formset, change):
        super().save_related(request, formset, change)  # Call the superclass method
        for form in formset.forms:
            if form.instance.pk is None:  # New object
                form.instance.user = request.user  # Assign request user
            form.save()  # Save the form data

@admin.register(YourModel)  # Replace with your parent model
class YourModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
