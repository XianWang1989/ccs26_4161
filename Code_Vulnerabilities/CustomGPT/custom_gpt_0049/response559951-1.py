
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Pop the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StuffForm, self).save(commit=False)

        if self.request:
            # Access the request object and modify your instance
            instance.user = self.request.user

        if commit:
            instance.save()

        return instance

class StuffInline(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        # Pass the request object to the form
        formset = super(StuffInline, self).get_formset(request, obj, **kwargs)
        formset.form.request = request
        return formset

class StuffAdmin(admin.ModelAdmin):
    inlines = [StuffInline]

admin.site.register(StuffModel, StuffAdmin)
