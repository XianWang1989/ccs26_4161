
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def save(self, commit=True):
        # Access the request object if needed
        if hasattr(self, 'request'):
            # Perform actions using the request object
            self.instance.user = self.request.user  # Example of setting user
        return super().save(commit=commit)

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        # Pass the request to the form
        formset.form.request = request
        return formset

@admin.register(YourParentModel)
class YourParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
