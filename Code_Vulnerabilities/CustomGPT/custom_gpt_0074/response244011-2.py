
def test_logging(request):
    logr = logging.getLogger(__name__)
    logr.debug("Testing logging...")
    return HttpResponse("Check your log file for the output!")
