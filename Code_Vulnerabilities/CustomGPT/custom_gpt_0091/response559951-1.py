
from django.contrib import admin
from django import forms
from myapp.models import StuffModel  # replace with your actual model

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # include your model's fields

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, form, formset, change):
        super().save_related(request, form, formset, change)
        for obj in formset.save(commit=False):
            # Access request here and set other fields as necessary
            obj.user = request.user  # or any other attribute you need
            obj.save()

@admin.register(YourMainModel)  # replace with your main model
class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
