
from django.contrib import admin
from django import forms
from .models import StuffModel  # Adjust this import according to your app structure

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust fields as necessary


class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formset, change):
        super().save_related(request, form, formset, change)

        # Access each object in the formset and update it
        for obj in formset.save(commit=False):
            obj.user = request.user  # or any other attribute you want to set
            obj.save()
        formset.save_m2m()  # If you are using ManyToMany fields


@admin.register(YourMainModel)  # Replace with your actual main model
class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
