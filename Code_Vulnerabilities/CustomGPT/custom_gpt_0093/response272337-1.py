
import logging
from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Configure logging
    logging_config = config.get_settings().get('logging_config')
    if logging_config:
        logging.config.fileConfig(logging_config)

    # Your app setup here

    return config.make_wsgi_app()
