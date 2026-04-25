
from pyramid.config import Configurator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_database_connection():
    DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)

    return Session()

def main():
    with Configurator() as config:
        config.add_route('home', '/')

        # Use the connection
        session = get_database_connection()
        # Do something with the session

    return config.make_wsgi_app()
