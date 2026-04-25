
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
        # This method gets called before saving related objects
        super().save_related(request, form, formsets, change)

        # Access the inline object
        for formset in formsets:
            for obj in formset.save(commit=False):
                # Update your instance here
                obj.user = request.user  # Assigning the request user before saving
                obj.save()  # Save the instance

class MyAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyModel, MyAdmin)
