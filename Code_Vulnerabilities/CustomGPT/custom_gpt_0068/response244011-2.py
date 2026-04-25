
import logging
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

@csrf_exempt  # Depending on your requirements
def login(request):
    logger.debug("Debug: Entering the login view")
    # Your login logic here
    # Simulate an action to log
    logger.info("User attempted to log in.")
    c = {}
    c.update(csrf(request))
    return render_to_response('accounts/login.html', c)
