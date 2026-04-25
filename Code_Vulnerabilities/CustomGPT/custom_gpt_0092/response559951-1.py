
from django.contrib import admin
from django import forms
from myapp.models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

    def save(self, commit=True):
        # Here, you can access the request if you set it in the form's init method
        instance = super().save(commit=False)
        # do something with self.request, e.g., set user
        if hasattr(self, 'request'):
            instance.user = self.request.user
        if commit:
            instance.save()
        return instance

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.request = request  # Pass the request to the form
        return formset

# Register your ModelAdmin with the inline
class MyModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourModel, MyModelAdmin)
