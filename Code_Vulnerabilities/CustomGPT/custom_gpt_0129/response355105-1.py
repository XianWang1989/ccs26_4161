
import logging

# Configure logging
logger = logging.getLogger(__name__)

def my_view(request):
    logger.info("Received request for my_view")

    try:
        # Your view logic here
        return HttpResponse("Hello, World!")

    except Exception as e:
        logger.error("Error processing request: %s", str(e))
        return HttpResponseServerError("Internal server error.")
