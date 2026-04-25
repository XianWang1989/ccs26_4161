
from pyramid.config import Configurator
import postgresql

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Database connection
    try:
        db = postgresql.open("pq://username:password@127.0.0.1:5432/db_name")
        config.add_request_method(lambda request: db, 'db', reify=True)
    except postgresql.exceptions.ClientCannotConnectError as e:
        print(f"Unable to connect to the database: {e}")

    # Other Pyramid setup
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
