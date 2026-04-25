
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^browse/', include('media.urls')),  # This can remain unchanged if used correctly
    url(r'^admin/', admin.site.urls),
)
