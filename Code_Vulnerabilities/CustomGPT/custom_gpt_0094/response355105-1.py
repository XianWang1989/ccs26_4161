
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    logger.debug("Request received at my_view.")
    # Your view logic here
    return HttpResponse("Hello, Django!")
