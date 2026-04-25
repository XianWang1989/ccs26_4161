
# admin.py
from django.contrib import admin
from tribes.models import YourModel  # Ensure YourModel exists in models.py

admin.site.register(YourModel)
