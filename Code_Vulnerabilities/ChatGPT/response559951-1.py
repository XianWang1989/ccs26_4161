
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

# Custom form for your inline model
class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust fields as necessary

    def save(self, commit=True):
        # Access request object if needed. You can store it when initializing the form.
        if hasattr(self, 'request'):
            # Example usage
            self.instance.user = self.request.user  # Store the user if necessary
        return super(StuffForm, self).save(commit=commit)

# Custom formset to pass the request
class StuffFormSet(forms.BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(StuffFormSet, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        for form in self.forms:
            if self.request:
                form.request = self.request  # Attach the request to the form
            form.save(commit=commit)

# Your GenericStackedInline using the custom formset
class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request  # Passing the request to the formset
        return formset

# Example of the parent admin class
class ParentModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

# Register your parent admin
admin.site.register(ParentModel, ParentModelAdmin)
