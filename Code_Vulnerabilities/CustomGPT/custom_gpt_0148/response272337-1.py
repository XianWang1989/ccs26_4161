
import logging
import logging.config
from pyramid.config import Configurator

def main(global_config, **settings):
    # Load logging configuration
    logging.config.fileConfig(settings['logging_config'])

    # Example usage
    logger = logging.getLogger('sqlalchemy.engine')
    logger.info("This is an info message.")

    # Rest of your Pyramid setup
    config = Configurator(settings=settings)
    return config.make_wsgi_app()
