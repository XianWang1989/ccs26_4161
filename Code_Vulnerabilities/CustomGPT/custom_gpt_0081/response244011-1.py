
# In your apps.py file:
import logging

logger = logging.getLogger(__name__)

class YourAppConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        logger.debug("Logging from ready method")
