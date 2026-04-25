
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(StuffForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # Here you can access the request object
        if self.request:
            instance = super(StuffForm, self).save(commit=False)
            # Do something with the request, for example:
            instance.user = self.request.user  # Set the user before saving
            if commit:
                instance.save()
            return instance
        return super(StuffForm, self).save(commit)

class StuffAdmin(admin.TabularInline):  # Use TabularInline or StackedInline
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(StuffAdmin, self).get_formset(request, obj, **kwargs)
        # Pass the request to the form
        formset.form.request = request
        return formset

@admin.register(YourMainModel)
class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
