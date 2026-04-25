
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^browse/', include('media.urls')),  # Ensure this includes the trailing slash
    url(r'^admin/', admin.site.urls),  # Fix for admin pattern
)
