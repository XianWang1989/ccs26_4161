
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel  # Assuming StuffModel is your model

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Pop the request object from kwargs
        self.request = kwargs.pop('request', None)
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # Here 'self.instance' is the model object being saved
        if self.request:
            self.instance.user = self.request.user  # Example: associate model with the user
        return super(StuffForm, self).save(commit)

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        # Pass request to the form's kwargs
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        formset.form_kwargs['request'] = request
        return formset

class MainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainModelAdmin)  # Register the main model
