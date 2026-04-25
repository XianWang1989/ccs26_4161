
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

    def save_formset(self, request, form, formset, change):
        super().save_formset(request, form, formset, change)
        for obj in formset.save(commit=False):
            # Here you can access the request object
            obj.user = request.user  # or any other logic
            obj.save()

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)
