
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^browse/', include('media.urls')),  # Correctly include media URLs
    url(r'^admin/', admin.site.urls),          # Use admin.site.urls instead of include
]
