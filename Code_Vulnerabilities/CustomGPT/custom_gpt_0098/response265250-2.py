
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def connect_db():
    # Use TCP/IP connection
    db = postgresql.open('pq://username:password@localhost:5432/db_name')
    return db

def my_view(request):
    db = connect_db()
    # Perform database operations
    return Response("Database connection successful!")

if __name__ == '__main__':
    config = Configurator()
    config.add_route('home', '/')
    config.add_view(my_view, route_name='home')
    app = config.make_wsgi_app()
    # (run the application as needed)
