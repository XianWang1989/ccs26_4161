
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel, MediaItem  # Adjust import based on your models

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Include fields as required

    def save(self, commit=True):
        # Access the request object if it's passed
        request = self._request
        obj = super(StuffForm, self).save(commit=False)
        obj.user = request.user  # Set user or other fields as necessary

        if commit:
            obj.save()

        return obj

    def __init__(self, *args, **kwargs):
        self._request = kwargs.pop('request', None)  # Capture request object
        super(StuffForm, self).__init__(*args, **kwargs)


class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        # Pass the request to the formset's form
        formset.request = request
        return formset

    def formset_valid(self, formset):
        formset.request = self.request  # Ensure request is available in formset
        return super(StuffAdmin, self).formset_valid(formset)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.request = request  # Attach the request to form
        return form

# Register your models as needed
class MediaItemAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MediaItem, MediaItemAdmin)
