
import logging
import logging.config
from pyramid.config import Configurator

# Assuming this dictionary is parsed from the INI config you provided
log_config = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': [],
        },
    }
}

def main(global_config, **settings):
    logging.config.dictConfig(log_config)  # Setup logging configuration
    logger = logging.getLogger('sqlalchemy.engine')
    logger.info("This is an info message from SQLAlchemy engine.")

    config = Configurator(settings=settings)
    # Add routes, views, etc.

    return config.make_wsgi_app()
