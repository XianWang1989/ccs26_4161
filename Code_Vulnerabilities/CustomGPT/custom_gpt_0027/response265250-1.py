
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def db_connect():
    try:
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return db
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def my_view(request):
    db = db_connect()
    if db:
        return Response("Connected to the database!")
    else:
        return Response("Database connection failed.")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('my_view', '/')
        config.add_view(my_view, route_name='my_view')
        app = config.make_wsgi_app()
