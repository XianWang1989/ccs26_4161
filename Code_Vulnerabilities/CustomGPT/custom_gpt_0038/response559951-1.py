
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

class StuffModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # other fields...

class StuffForm(forms.ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'

class StuffAdmin(GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_formset(self, request, formset, change):
        super().save_formset(request, formset, change)
        for form in formset.forms:
            obj = form.save(commit=False)
            obj.user = request.user  # Assign the current user
            obj.save()

@admin.register(YourMainModel)
class YourMainModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]
