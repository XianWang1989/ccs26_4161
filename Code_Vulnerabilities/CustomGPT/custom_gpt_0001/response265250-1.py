
import os
import sys
from pyramid.config import Configurator
from pyramid.wsgi import get_app

# Add the path to your Pyramid app
sys.path.insert(0, "/var/www/my_pyramid_app")

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application. """
    config = Configurator(settings=settings)
    config.include('my_pyramid_app')
    return config.make_wsgi_app()

# Change the permissions for the PostgreSQL socket
os.chmod("/var/run/postgresql/.s.PGSQL.5432", 0o770)

application = main({}, **{
    'pyramid.includes': 'pyramid_chameleon',
    'sqlalchemy.url': 'postgresql://username:password@localhost/db_name'
})
