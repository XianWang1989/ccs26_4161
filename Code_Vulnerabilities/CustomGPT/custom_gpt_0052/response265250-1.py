
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Setup database connection
    engine = engine_from_config(settings, 'sqlalchemy.')

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Store session in the app registry
    config.registry.session_factory = Session

    # Add your routes and views here

    return config.make_wsgi_app()
