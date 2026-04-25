
import logging.config
from pyramid.config import Configurator

def main(global_config, **settings):
    logging.config.fileConfig('development.ini')

    config = Configurator(settings=settings)

    # Your pyramid app setup code (views, routes, etc.)
    return config.make_wsgi_app()
