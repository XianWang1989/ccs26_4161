
from django.contrib import admin
from django.forms import ModelForm
from .models import StuffModel  # Adjust this import according to your project structure

class StuffForm(ModelForm):
    class Meta:
        model = StuffModel
        fields = '__all__'  # Adjust fields as necessary

class StuffAdmin(admin.GenericStackedInline):
    model = StuffModel
    form = StuffForm

    def save_related(self, request, formset, change):
        # Iterate through each form in the formset
        for form in formset.forms:
            obj = form.save(commit=False)  # Do not commit yet
            obj.user = request.user  # Set the user before saving
            obj.save()  # Now save the object

class MyModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MyMainModel, MyModelAdmin)  # Replace MyMainModel with your main model
