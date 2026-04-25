
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^browse/', include('media.urls')),  # Ensure trailing slash
    url(r'^admin/', admin.site.urls),
]
