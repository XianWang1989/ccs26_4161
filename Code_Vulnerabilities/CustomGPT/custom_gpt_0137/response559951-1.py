
from django.contrib import admin
from django import forms
from myapp.models import ParentModel, StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formsets, change):
        # Iterate through the formsets to access each instance being saved
        super().save_related(request, form, formsets, change)

        # Now formsets will contain the inline forms
        for formset in formsets:
            for obj in formset.save(commit=False):  # Use commit=False to avoid saving immediately
                # Here you can use the request object to update the obj
                obj.user = request.user  # Set an attribute, for example
                obj.save()  # Now save the object

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)
