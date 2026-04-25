
import logging
from pyramid.config import Configurator

# Example logging configuration
def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Logging configuration
    config.add_settings({
        'logger_sqlalchemy.level': 'INFO',
        'logger_sqlalchemy.handlers': '',
        'logger_sqlalchemy.quename': 'sqlalchemy.engine',
    })

    return config.make_wsgi_app()

if __name__ == "__main__":
    app = main({})
    # Example of using the logger
    logger = logging.getLogger('sqlalchemy.engine')
    logger.info('This is an info message.')
