
import logging
from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Set up logging
    logging.config.fileConfig('logging.ini')  # Assuming your settings are in `logging.ini`

    return config.make_wsgi_app()
