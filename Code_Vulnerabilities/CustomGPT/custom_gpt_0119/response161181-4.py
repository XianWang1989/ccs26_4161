
from django.contrib import admin
from .models import YourModel  # Adjust this to your actual model name

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Adjust fields accordingly

admin.site.register(YourModel, YourModelAdmin)
