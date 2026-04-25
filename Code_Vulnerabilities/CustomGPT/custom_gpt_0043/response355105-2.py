
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def home(request):
    logger.info("Home page accessed")
    return HttpResponse("Hello, World!")
