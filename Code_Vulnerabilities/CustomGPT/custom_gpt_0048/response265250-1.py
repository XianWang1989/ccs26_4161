
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def db_connection():
    db = postgresql.open('pq://username:password@localhost/db_name')
    return db

def hello_world(request):
    db = db_connection()
    query = "SELECT * FROM my_table LIMIT 10;"
    result = db.query(query)
    return Response(str(result))

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()

