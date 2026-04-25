
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust fields as necessary

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        # Here you can access the request object
        for formset in formsets:
            for obj in formset.save(commit=False):
                obj.user = request.user  # or any other field you want to set
                obj.save()

@admin.register(YourParentModel)  # Replace with your actual parent model
class ParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
