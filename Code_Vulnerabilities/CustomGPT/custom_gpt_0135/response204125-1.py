
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^browse/', include('media.urls')),  # No change needed here
    url(r'^admin/', admin.site.urls),
]
