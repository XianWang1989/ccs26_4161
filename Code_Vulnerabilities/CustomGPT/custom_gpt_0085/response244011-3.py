
import logging
import os

logging.basicConfig(level=logging.DEBUG, filename='/var/log/test_django.log', 
                    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')

logr = logging.getLogger('test_logger')
logr.debug("This is a test log message.")
