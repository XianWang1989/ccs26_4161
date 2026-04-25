
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

class StuffModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # other fields...

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)  # Get the instance
        if self.request:  # Check if request is available
            instance.user = self.request.user  # Set the user
        if commit:
            instance.save()
        return instance

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request  # Pass the request to the formset
        return formset

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.request = request  # Pass the request to the form
        return form
