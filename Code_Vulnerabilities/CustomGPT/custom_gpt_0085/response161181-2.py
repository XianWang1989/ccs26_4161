
from django.contrib import admin
from .models import YourModelName  # Adjust according to your model names

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Adjust fields as necessary

admin.site.register(YourModelName, YourModelAdmin)
