
from pyramid.config import Configurator
import postgresql

def connect_to_db():
    try:
        # Replace with your actual connection string
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        print(f"Connection error: {e}")
        return None

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Connect to the database
    db_connection = connect_to_db()
    if db_connection:
        print("Database connection established successfully.")

    return config.make_wsgi_app()
