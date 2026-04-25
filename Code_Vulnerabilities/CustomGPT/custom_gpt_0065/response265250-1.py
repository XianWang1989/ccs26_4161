
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def db_connection(request):
    try:
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return Response("Database connection successful!")
    except Exception as e:
        return Response(f"Connection error: {e}")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('test_db', '/test_db')
        config.add_view(db_connection, route_name='test_db')
        app = config.make_wsgi_app()
