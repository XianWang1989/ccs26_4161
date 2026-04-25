
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('browse/', include('media.urls')),
    path('admin/', admin.site.urls),
]
