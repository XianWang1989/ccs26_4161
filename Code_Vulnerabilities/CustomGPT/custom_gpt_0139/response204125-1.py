
url(r'^videos', ListView.as_view(
        queryset=Video.objects.all().order_by("-created")[:2],
        template_name="media.html")),
