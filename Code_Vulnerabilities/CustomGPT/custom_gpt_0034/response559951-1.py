
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import StuffModel

class StuffAdmin(GenericStackedInline):
    model = StuffModel

    def save_related(self, request, formset, change):
        super().save_related(request, formset, change)

        # Access the objects from the formset and update them
        for obj in formset.save(commit=False):
            obj.user = request.user  # Assign the request user to the object
            obj.save()

class StuffModelAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(YourParentModel, StuffModelAdmin)
