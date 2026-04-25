
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Database setup
    engine = engine_from_config(settings, 'sqlalchemy.')
    Session = sessionmaker(bind=engine)

    config.registry.session_factory = Session

    # Your routes and views...
    return config.make_wsgi_app()
