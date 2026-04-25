
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid import request

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Setup database connection
    db_url = 'postgresql://username:password@localhost:5432/db_name'
    engine = engine_from_config(settings, 'sqlalchemy.')

    # Add your views and routes here
    config.add_route('home', '/')

    return config.make_wsgi_app()

if __name__ == '__main__':
    app = main({})
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
