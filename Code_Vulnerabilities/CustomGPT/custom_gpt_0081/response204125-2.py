
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('browse/', include('media.urls')),
    path('admin/', admin.site.urls),
]
