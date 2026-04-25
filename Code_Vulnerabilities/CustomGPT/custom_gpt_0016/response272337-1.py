
import logging
from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Set up logging
    logging.config.fileConfig('logging.ini')  # Assume 'logging.ini' contains your configuration

    # Your application setup code here
    return config.make_wsgi_app()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('sqlalchemy.engine').info('This is an example SQLAlchemy log message.')
