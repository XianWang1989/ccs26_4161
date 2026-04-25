
url(r'^videos', ListView.as_view(...)),
url(r'^videos/(?P<pk>\d+)$', DetailView.as_view(...)),
