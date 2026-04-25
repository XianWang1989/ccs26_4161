
from django.http import HttpResponse

def test_logging(request):
    logr.info("Test logging endpoint accessed.")
    return HttpResponse("Check your log file!")
