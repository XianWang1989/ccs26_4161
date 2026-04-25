
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, formset, change):
        super().save_related(request, formset, change)
        for obj in formset.save():
            obj.user = request.user  # Assign the request user to the model
            obj.save()

class MyMainAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyMainModel, MyMainAdmin)
