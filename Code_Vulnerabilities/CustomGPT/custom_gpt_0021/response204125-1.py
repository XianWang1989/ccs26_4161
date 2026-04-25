
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('browse/', include('media.urls')),  # Added trailing slash
    path('admin/', admin.site.urls),
]
