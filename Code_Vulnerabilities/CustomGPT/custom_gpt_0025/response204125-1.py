
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^browse/', include('media.urls')),  # Correctly includes media.urls
    url(r'^admin/', admin.site.urls),          # Corrected admin import
]
