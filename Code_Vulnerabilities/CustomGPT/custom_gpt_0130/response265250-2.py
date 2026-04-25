
from pyramid.config import Configurator
import postgresql

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Initialize database connection
    db = postgresql.open('pq://username:password@localhost:5432/db_name')

    return config.make_wsgi_app()
