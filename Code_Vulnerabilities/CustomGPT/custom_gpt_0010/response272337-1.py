
import logging
import logging.config
from pyramid.config import Configurator

# Assuming the config is loaded from an .ini file.
def main():
    config = Configurator()

    # Load logging configuration
    logging.config.fileConfig('logging.conf')  # Your config file

    # Create a logger
    logger = logging.getLogger('sqlalchemy.engine')

    # Example usage of the logger
    logger.info("This is an info message from SQLAlchemy.")

if __name__ == '__main__':
    main()
