
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^browse/', include('media.urls')),  # Correctly includes media urls
    url(r'^admin/', admin.site.urls),         # Updated for Django versions >= 1.10
)
