
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Database setup
    db_url = settings.get('sqlalchemy.url', 'postgresql://username:password@localhost/db_name')
    config.registry.db_engine = engine_from_config(settings, 'sqlalchemy.')

    # Other configurations...

    return config.make_wsgi_app()
