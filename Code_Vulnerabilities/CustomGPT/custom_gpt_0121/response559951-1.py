
from django.contrib import admin
from django import forms
from your_app.models import StuffModel  # Replace with your actual model

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, formset, change):
        # Accessing the instances from the formset
        for obj in formset.save(commit=False):
            # Here you can modify the object before saving
            obj.user = request.user  # Or any other attribute you want to set
            obj.save()
        formset.save_m2m()  # Save many-to-many relationships if needed

class MainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MainModel, MainAdmin)  # Replace MainModel with your actual model
