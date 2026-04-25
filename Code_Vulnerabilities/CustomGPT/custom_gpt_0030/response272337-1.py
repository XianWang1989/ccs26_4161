
import logging
from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Set up logging based on the provided configuration
    logging.config.fileConfig('your_config_file.ini')

    # Example usage of the logger
    logger = logging.getLogger('sqlalchemy.engine')
    logger.info('SQLAlchemy engine logger is set up.')

    return config.make_wsgi_app()
