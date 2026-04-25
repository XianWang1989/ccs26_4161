
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline

# Your model
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffInline(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, formset, change):
        super().save_related(request, formset, change)
        for form in formset.forms:
            if form.instance.pk is None:  # only for new objects
                form.instance.user = request.user  # Set user or other attributes
                form.instance.save()

class YourAdmin(admin.ModelAdmin):
    inlines = [StuffInline]

admin.site.register(YourModel, YourAdmin)
