
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get request object
        super(StuffForm, self).__init__(*args, **kwargs)

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form = self.form  # Replace form with our custom form
        return formset

    def save_related(self, request, form, formset, change):
        # Iterate over the formset to access each obj
        for obj in formset.save(commit=False):
            obj.user = request.user  # Assign the user from the request
            obj.save()  # Now save the object
        formset.save_m2m()  # Save many-to-many relations if there are any

# Finally, register your admin class
class MyAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyModel, MyAdmin)
