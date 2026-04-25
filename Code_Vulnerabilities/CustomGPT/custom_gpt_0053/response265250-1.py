
import os
import logging
from pyramid.config import Configurator
import postgresql

# Set up logging
logging.basicConfig(level=logging.INFO)

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Connect to PostgreSQL
    try:
        db_url = os.environ.get('DATABASE_URL', 'pq://username:password@localhost:5432/db_name')
        db = postgresql.open(db_url)
        logging.info("Database connection successful.")
    except Exception as e:
        logging.error("Database connection failed: %s", e)

    # Continue configuring your Pyramid application
    return config.make_wsgi_app()

if __name__ == '__main__':
    main({}, **{})
