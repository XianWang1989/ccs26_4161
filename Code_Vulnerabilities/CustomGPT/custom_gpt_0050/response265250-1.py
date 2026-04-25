
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def get_db_connection():
    try:
        db = postgresql.open("pq://username:password@localhost:5432/db_name")
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        print(f"Connection error: {e}")
        return None

def my_view(request):
    db = get_db_connection()
    if db:
        # Perform database operations here
        return Response("Database connected!")
    return Response("Failed to connect to the database.", status=500)

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('my_view', '/')
    config.add_view(my_view, route_name='my_view')
    return config.make_wsgi_app()
