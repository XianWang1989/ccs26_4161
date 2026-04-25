
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^browse/', include('media.urls')),  # Ensure 'media.urls' is correctly targeted
    url(r'^admin/', admin.site.urls),  # Note: You can use admin.site.urls directly
]
