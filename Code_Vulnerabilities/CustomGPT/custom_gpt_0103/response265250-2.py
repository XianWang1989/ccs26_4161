
from pyramid.config import Configurator
from postgresql import connect

def get_database_connection():
    db_url = "pq://username:password@127.0.0.1:5432/db_name"
    return connect(db_url)

def main(global_config, **settings):
    config = Configurator(settings=settings)
    connection = get_database_connection()
    return config.make_wsgi_app()
