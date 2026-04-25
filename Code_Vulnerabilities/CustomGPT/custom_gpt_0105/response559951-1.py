
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in instances:
            # Access the request object here
            obj.user = request.user  # Example: Attach the user to the instance
            obj.save()
        formset.save_m2m()  # Save many-to-many relationships if needed

class MyModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

# Register your admin class
admin.site.register(MyModel, MyModelAdmin)
