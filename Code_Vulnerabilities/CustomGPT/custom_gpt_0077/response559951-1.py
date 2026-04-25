
from django.contrib import admin
from django import forms
from yourapp.models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request  # Store the request in the formset
        return formset

    def save_related(self, request, form, formset, change):
        super().save_related(request, form, formset, change)
        for obj in formset.save(commit=False):
            # Here you can access the request object
            obj.user = request.user  # Set user or any other attribute
            obj.save()

class MyAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyModel, MyAdmin)
