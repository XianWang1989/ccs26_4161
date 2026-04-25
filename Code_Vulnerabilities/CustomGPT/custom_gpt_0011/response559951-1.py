
from django import forms
from django.contrib import admin
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(StuffForm, self).save(commit=False)
        if self.request:  # Check if request is available
            obj.user = self.request.user  # Set the user or any other attribute
        if commit:
            obj.save()
        return obj

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.request = request  # Store the request in the formset
        return formset

# In your main admin class
class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainAdmin)
