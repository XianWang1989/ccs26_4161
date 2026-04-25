
import logging

logger = logging.getLogger(__name__)

def login(request):
    logger.debug("THIS BETTER WORK >:O")
    c = {}
    c.update(csrf(request))
    return render_to_response('accounts/login.html', c)
