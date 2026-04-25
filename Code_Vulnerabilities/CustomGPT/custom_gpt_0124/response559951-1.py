
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        # Here, you can access the request object
        instances = formset.save(commit=False)
        for obj in instances:
            # Do something with the request
            obj.user = request.user  # Example: set user from request
            obj.save()
        formset.save_m2m()  # Save many-to-many relationships if applicable

class ParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentAdmin)
