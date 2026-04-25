
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from media.models import Video

urlpatterns = [
    url(r'^videos/', ListView.as_view(
            queryset=Video.objects.all().order_by("-created")[:2],
            template_name="media.html")),
    url(r'^videos/(?P<pk>\d+)/$', DetailView.as_view(
            model=Video,
            template_name="video.html")),
]
