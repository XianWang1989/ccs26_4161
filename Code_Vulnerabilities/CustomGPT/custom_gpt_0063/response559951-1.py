
from django.contrib import admin
from django import forms
from yourapp.models import StuffModel, YourParentModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm
    extra = 1  # Number of extra empty forms to display

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            for obj in formset.save(commit=False):
                obj.user = request.user  # Access the request object here
                obj.save()

@admin.register(YourParentModel)
class YourParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
