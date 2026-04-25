import logging

logger = logging.getLogger(__name__)

def test_logging(request):
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    return HttpResponse("Logging test complete.")
