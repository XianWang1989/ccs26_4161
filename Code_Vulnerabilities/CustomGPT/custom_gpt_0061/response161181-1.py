
from django.contrib import admin
from .models import YourModel  # Replace YourModel with actual model names.

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with actual fields.

admin.site.register(YourModel, YourModelAdmin)
