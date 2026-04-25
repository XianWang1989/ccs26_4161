
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust fields as necessary

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formset, change):
        # Retrieve the instance before saving
        instances = formset.save(commit=False)

        for obj in instances:
            # Here you can set attributes on obj
            obj.user = request.user  # Example: setting the user
            obj.save()

        # Call the parent class's save_related to handle any additional saving
        super().save_related(request, form, formset, change)

class MyModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyModel, MyModelAdmin)
