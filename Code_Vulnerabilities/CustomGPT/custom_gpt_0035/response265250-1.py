
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Setup the database connection
    db_url = settings['sqlalchemy.url']
    engine = engine_from_config(settings, 'sqlalchemy.')

    config.add_route('home', '/')
    config.scan()

    return config.make_wsgi_app()
