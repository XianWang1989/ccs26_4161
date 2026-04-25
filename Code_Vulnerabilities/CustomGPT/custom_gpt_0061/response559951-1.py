
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.StackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, formset, change):
        # Iterate through the formset and update the instance before saving
        instances = formset.save(commit=False)
        for obj in instances:
            # Here you can access the request object
            obj.user = request.user  # For example, assign the user
            obj.save()  # Saving the object
        formset.save_m2m()  # Save many-to-many fields if necessary

class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(ParentModel, ParentModelAdmin)
