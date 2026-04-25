
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get the request object
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StuffForm, self).save(commit=False)

        # You can now access the request object using self.request
        if self.request:
            instance.user = self.request.user  # Example: setting user before saving

        if commit:
            instance.save()
        return instance

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        # Pass the request object to the formset
        formset.form = self.get_form_with_request(request)
        return formset

    def get_form_with_request(self, request):
        # This method creates a form that passes the request to the form class
        class FormWithRequest(self.form):
            def __init__(self, *args, **kwargs):
                kwargs['request'] = request
                super(FormWithRequest, self).__init__(*args, **kwargs)

        return FormWithRequest

# Register your admin class in the Django Admin
@admin.register(StuffModel)
class StuffModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
