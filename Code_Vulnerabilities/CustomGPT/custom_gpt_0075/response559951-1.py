
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

        # Here, you can access the request object and update your instance
        obj = form.instance  # Get the instance of the model being edited
        obj.user = request.user  # Update with the request user
        obj.save()  # Save the object with the updated information    

class MyAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
