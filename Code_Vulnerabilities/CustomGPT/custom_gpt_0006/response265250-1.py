
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def db_connect():
    try:
        # Replace 'username', 'password', 'db_name' with actual values
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        return Response(f"Database connection failed: {e}")

def hello_world(request):
    db = db_connect()
    if isinstance(db, Response):
        return db
    return Response("Hello, World!")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
