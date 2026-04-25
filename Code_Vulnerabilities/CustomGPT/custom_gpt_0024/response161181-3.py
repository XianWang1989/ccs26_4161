
# admin.py

from django.contrib import admin
from tribes.models import YourModel  # Ensure YourModel exists in models.py

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Adjust based on your model fields

admin.site.register(YourModel, YourModelAdmin)
