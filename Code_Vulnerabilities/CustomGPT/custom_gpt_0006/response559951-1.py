
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.TabularInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            # Access request.user or any other request attributes here
            instance.user = request.user  # Example: setting the user
            instance.save()
        formset.save_m2m()  # Save many-to-many relationships if any

class ParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentAdmin)
