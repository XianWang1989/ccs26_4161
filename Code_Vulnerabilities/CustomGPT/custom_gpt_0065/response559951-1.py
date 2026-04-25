
from django.contrib import admin
from django import forms
from .models import StuffModel  # Replace with your actual model

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, formset, change):
        super().save_related(request, formset, change)
        # Here you can access the request object and modify instance(s)
        for obj in formset.save(commit=False):
            obj.user = request.user  # Example: set the user
            obj.save()

class ParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentAdmin)  # Replace with your actual parent model
