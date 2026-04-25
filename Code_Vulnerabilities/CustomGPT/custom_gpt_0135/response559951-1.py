
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

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            if isinstance(formset, self.__class__):
                for obj in formset.save(commit=False):
                    obj.user = request.user  # Access the request object
                    obj.save()

@admin.register(YourMainModel)  # Replace with your main model
class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
