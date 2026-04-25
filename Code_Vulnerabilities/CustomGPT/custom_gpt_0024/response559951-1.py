
from django.contrib import admin
from django import forms
from django.contrib.contenttypes.admin import GenericStackedInline

class StuffModel(models.Model):
    # Your model fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract request
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StuffForm, self).save(commit=False)
        if self.request:
            instance.user = self.request.user  # Assign request.user
        if commit:
            instance.save()
        return instance

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request  # Pass request to formset
        return formset

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.request = request  # Pass request to form
        return form
