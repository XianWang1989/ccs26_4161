
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('browse/', include('media.urls')),  # Use path instead of url for Django 2.x+
    path('admin/', admin.site.urls),
]
