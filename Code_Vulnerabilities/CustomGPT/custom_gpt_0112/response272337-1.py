
import logging
from pyramid.config import Configurator

# Example configuration for Pyramid logging
def setup_logging():
    logging.config.fileConfig('your_config.ini')  # Points to your INI file
    logger = logging.getLogger('sqlalchemy.engine')
    logger.info("SQLAlchemy logging started.")

if __name__ == "__main__":
    setup_logging()
