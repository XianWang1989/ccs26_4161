
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def db_connection():
    try:
        # Replace with your actual database details
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return db
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def my_view(request):
    db = db_connection()
    if db:
        # Perform database operations here
        return Response("Database connection successful")
    else:
        return Response("Failed to connect to database.", status=500)

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('my_view', '/')
        config.add_view(my_view, route_name='my_view')
        app = config.make_wsgi_app()
