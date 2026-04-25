
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

    def save_formset(self, request, formset, change):
        # Iterate through each form in the formset
        for form in formset.forms:
            if form.is_valid():
                # Access the object and assign the request.user or any other attribute
                obj = form.save(commit=False)
                obj.user = request.user  # Example: setting the user before saving
                obj.save()  # Save the instance
        super().save_formset(request, formset, change)

class ParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
