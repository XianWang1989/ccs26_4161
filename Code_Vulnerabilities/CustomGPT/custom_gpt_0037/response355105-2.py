
import logging

logger = logging.getLogger(__name__)

def some_view(request):
    try:
        # Your view logic
        pass
    except Exception as e:
        logger.error("An error occurred: %s", e)
        return HttpResponse("Error occurred")
