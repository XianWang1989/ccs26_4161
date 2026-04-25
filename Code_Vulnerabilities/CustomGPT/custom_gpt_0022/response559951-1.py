
from django.contrib import admin
from django import forms
from yourapp.models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def save(self, commit=True):
        # Access the request object if passed
        if hasattr(self, 'request'):
            # Example of using request.user
            self.instance.user = self.request.user
        return super(StuffForm, self).save(commit=commit)

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Attach the request to the form
        return formset

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainAdmin)
