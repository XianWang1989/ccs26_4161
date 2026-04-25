
from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from media.models import Video

urlpatterns = patterns('',
    url(r'^videos/$', ListView.as_view(
            queryset=Video.objects.all().order_by("-created")[:2],
            template_name="media.html"), name='video-list'),
    url(r'^videos/(?P<pk>\d+)/$', DetailView.as_view(
            model=Video,
            template_name="video.html"), name='video-detail'),
)
