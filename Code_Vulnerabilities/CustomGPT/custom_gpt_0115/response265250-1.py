
import logging
from pyramid.config import Configurator
from postgresql import open as open_pg

logging.basicConfig(level=logging.INFO)

def get_db_connection():
    try:
        db = open_pg('pq://username:password@localhost:5432/db_name')
        return db
    except Exception as e:
        logging.error(f"Database connection error: {e}")
        raise

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Example of using the database connection in a view
    config.add_route('home', '/')
    config.add_view(my_view, route_name='home')

    return config.make_wsgi_app()

def my_view(request):
    db = get_db_connection()
    # Do something with the database
    return {'data': 'Your data'}
