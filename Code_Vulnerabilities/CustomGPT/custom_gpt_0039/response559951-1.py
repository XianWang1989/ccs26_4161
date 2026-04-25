
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.TabularInline):  # or GenericStackedInline
    model = StuffModel
    form = StuffForm

    def save_related(self, request, formset, change):
        super().save_related(request, formset, change)

        # Accessing the objects from the formset
        for obj in formset.instance:
            # Update object using request
            obj.user = request.user  # Example of setting user
            obj.save()

class ParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentAdmin)
