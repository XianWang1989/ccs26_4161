
from django.contrib import admin
from tribes.models import YourModelName  # Ensure the model name is correct

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with your model fields

admin.site.register(YourModelName, YourModelAdmin)
