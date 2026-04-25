
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def db_connect():
    try:
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return db
    except Exception as e:
        return str(e)

def hello_world(request):
    db = db_connect()
    return Response(f'Connection Status: {db}')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_view(hello_world, path='/', renderer='string')
        app = config.make_wsgi_app()
