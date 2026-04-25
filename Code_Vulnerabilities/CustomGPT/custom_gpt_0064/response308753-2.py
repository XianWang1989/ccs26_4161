
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('web2py')
logger.debug("Executing SQL: %s", query)
