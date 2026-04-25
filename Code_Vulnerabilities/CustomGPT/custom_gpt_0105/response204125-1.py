
urlpatterns = patterns('',
    url(r'^browse/', include('media.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
