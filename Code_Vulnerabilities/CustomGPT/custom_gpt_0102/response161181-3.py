
# admin.py
from django.contrib import admin
from .models import Tribe  # Ensure this line is present

admin.site.register(Tribe)
