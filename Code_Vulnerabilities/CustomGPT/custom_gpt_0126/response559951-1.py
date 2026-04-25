
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.TabularInline):  # Use TabularInline or StackedInline as needed
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            # Now you can access the request object
            instance.user = request.user  # For example, set user before saving
            instance.save()
        formset.save_m2m()  # Save many-to-many relationships if any

class MainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainModelAdmin)
