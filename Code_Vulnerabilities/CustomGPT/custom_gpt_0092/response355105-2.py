
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("Django is up and running!", content_type="text/plain")
