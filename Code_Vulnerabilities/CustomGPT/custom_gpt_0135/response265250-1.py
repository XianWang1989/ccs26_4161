
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
import logging

logging.basicConfig(level=logging.INFO)

def get_db_session():
    # Connection string example
    db_url = 'postgresql://username:password@127.0.0.1:5432/db_name'
    engine = engine_from_config({'sqlalchemy.url': db_url}, prefix='sqlalchemy.')
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == '__main__':
    with Configurator() as config:
        # Other configuration settings
        config.add_route('home', '/')
        app = config.make_wsgi_app()

        # Example usage
        session = get_db_session()
        try:
            # Perform database operations
            result = session.execute("SELECT * FROM some_table")
            for row in result:
                print(row)
        finally:
            session.close()
