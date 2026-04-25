
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^browse/', include('media.urls')),  # This is correct
    url(r'^admin/', admin.site.urls),         # Updated to use admin.site.urls directly
)
