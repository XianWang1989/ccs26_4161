
from pyramid.config import Configurator
from postgresql import connect

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Assuming you have a connection string
    connection_string = "pq://username:password@localhost:5432/db_name"
    try:
        db = connect(connection_string)
        print("Database connection successful")
    except Exception as e:
        print(f"Error connecting to database: {e}")

    return config.make_wsgi_app()
