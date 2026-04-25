
from django.urls import path
from django.views.generic import ListView, DetailView
from media.models import Video

urlpatterns = [
    path('videos/', ListView.as_view(
            queryset=Video.objects.all().order_by('-created')[:2],
            template_name="media.html")),
    path('videos/<int:pk>/', DetailView.as_view(
            model=Video,
            template_name="video.html")),
]
