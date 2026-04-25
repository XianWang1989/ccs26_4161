
from pyramid.config import Configurator
import postgresql

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Set up database connection
    db = postgresql.open('pq://username:password@localhost:5432/db_name')

    config.add_route('home', '/')
    config.add_view(home_view, route_name='home')

    return config.make_wsgi_app()

def home_view(request):
    return {'message': 'Hello, world!'}
