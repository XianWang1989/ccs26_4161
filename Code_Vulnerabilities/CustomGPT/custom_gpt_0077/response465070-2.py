
import logging

logger = logging.getLogger(__name__)

# Check if credentials are loaded
logger.info('AWS_ACCESS_KEY: %s', os.environ.get('AWS_ACCESS_KEY'))
logger.info('AWS_SECRET_ACCESS_KEY: %s', os.environ.get('AWS_SECRET_ACCESS_KEY'))
