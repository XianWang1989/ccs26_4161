
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def db_connection():
    try:
        db = postgresql.open('pq://username:password@localhost/db_name')
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        return str(e)

def my_view(request):
    db = db_connection()
    if isinstance(db, str):  # Check if it's an error message
        return Response(db)
    else:
        # Perform database operations
        return Response("Connected to the database!")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(my_view, route_name='home')
        app = config.make_wsgi_app()
