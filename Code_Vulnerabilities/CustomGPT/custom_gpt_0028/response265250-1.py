
import os
import sys
from pyramid.config import Configurator

# Add your application path
sys.path.insert(0, '/path/to/your/app')

# Set the environment variable
os.environ['DATABASE_URL'] = 'postgresql://username:password@localhost/db_name'

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
