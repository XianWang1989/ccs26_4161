
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    logger.debug("Entering my_view function.")
    # Your view logic here
    logger.debug("Exiting my_view function.")
