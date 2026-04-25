
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^browse/', include('media.urls')),  # This pattern is correct
    url(r'^admin/', admin.site.urls),
]
