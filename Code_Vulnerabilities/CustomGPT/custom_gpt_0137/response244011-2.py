
import logging
logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK >:O")
    print("Login view called!")  # This will be visible in Apache error logs
    # Other code...
