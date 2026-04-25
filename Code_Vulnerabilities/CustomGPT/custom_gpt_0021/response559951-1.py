
from django.contrib import admin
from django import forms
from .models import StuffModel

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

class ParentAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

    def save_related(self, request, obj, form, change):
        super().save_related(request, obj, form, change)
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, StuffAdmin):
                for instance in inline.formset.save(commit=False):
                    # Access the request object here
                    instance.user = request.user  # Example usage
                    instance.save()

# Register the ParentAdmin
admin.site.register(ParentModel, ParentAdmin)
