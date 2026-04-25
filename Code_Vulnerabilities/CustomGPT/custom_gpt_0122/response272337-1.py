
import logging
from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Configure logging using the settings
    logging.config.fileConfig(settings['logging.config'])

    # Add your routes and views here

    return config.make_wsgi_app()
