from django.contrib import admin
from .models import StuffModel
from .forms import StuffForm

class StuffAdmin(admin.StackedInline):
    model = StuffModel
    form = StuffForm

    def get_formset(self, request, obj=None, **kwargs):
        # Inject request into the form class
        formset = super().get_formset(request, obj, **kwargs)
        for form in formset.forms:
            form.request = request  # Pass the request object to the form
        return formset

class MediaItemAdmin(admin.ModelAdmin):
    inlines = [StuffAdmin]

admin.site.register(MediaItem, MediaItemAdmin)
