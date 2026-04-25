
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def connect_db(request):
    try:
        # Adjust your connection string accordingly
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return Response("Connected to database successfully!")
    except Exception as e:
        return Response(f"Error connecting to database: {str(e)}")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('connect', '/connect')
        config.add_view(connect_db, route_name='connect')
        app = config.make_wsgi_app()

    # You can serve this with wsgi or another server
