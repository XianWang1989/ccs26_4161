
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel, YourMainModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, change, *args, **kwargs):
        super().save_related(request, form, change, *args, **kwargs)

        # Access the objects from the formset and assign the request user
        for obj in form.instance.stuffmodel_set.all():
            obj.user = request.user  # Assuming you have a user field in your model
            obj.save()

class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourMainModel, YourMainModelAdmin)
