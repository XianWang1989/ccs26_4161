
# mediasite/urls.py
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^browse/', include('media.urls')),
    url(r'^admin/', admin.site.urls),
)
