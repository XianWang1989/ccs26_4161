
from pyramid.config import Configurator
from pyramid.settings import aslist
import logging.config

# Assuming 'myapp.ini' is your configuration file
def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Load the logging configuration
    logging_config = settings['logger_sqlalchemy']
    logging.config.fileConfig(logging_config)

    return config.make_wsgi_app()
