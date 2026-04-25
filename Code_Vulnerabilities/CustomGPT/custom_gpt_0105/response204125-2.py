
urlpatterns = patterns('',
    url(r'^videos', ListView.as_view(...)),  # Missing trailing slash
    url(r'^videos/(?P<pk>\d+)$', DetailView.as_view(...)),
)
