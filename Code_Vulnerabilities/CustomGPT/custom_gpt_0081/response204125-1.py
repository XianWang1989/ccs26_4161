
from django.conf.urls import patterns, url  # Import corrected
from django.views.generic import ListView, DetailView
from media.models import Video

urlpatterns = patterns('',
    url(r'^videos/$', ListView.as_view(  # Added trailing slash here
            queryset=Video.objects.all().order_by("-created")[:2],
            template_name="media.html")),
    url(r'^videos/(?P<pk>\d+)/$', DetailView.as_view(  # Added trailing slash here
            model=Video,
            template_name="video.html")),
)
