
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
        instances = formset.save(commit=False)
        for obj in instances:
            # Update your instance here
            obj.user = request.user  # Example of using the request object
            obj.save()
        formset.save_m2m()  # Save many-to-many relationships

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)
