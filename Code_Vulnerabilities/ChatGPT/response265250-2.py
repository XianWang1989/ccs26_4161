
from pyramid.config import Configurator
import postgresql

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Connect to the PostgreSQL database
    db_url = 'pq://username:password@127.0.0.1:5432/db_name'
    db = postgresql.open(db_url)

    # Use the db connection in your application
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
