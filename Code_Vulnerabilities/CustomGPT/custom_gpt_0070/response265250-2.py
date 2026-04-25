
from pyramid.config import Configurator
import postgresql

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Establish database connection
    db = postgresql.open('pq://username:password@127.0.0.1:5432/db_name')

    # Add any other configuration as necessary
    return config.make_wsgi_app()
