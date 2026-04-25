
from pyramid.config import Configurator
from pyramid.response import Response
import psycopg2

def db_connect():
    try:
        connection = psycopg2.connect(
            dbname='db_name',
            user='your_user',
            password='your_password',
            host='localhost',
            port='5432'
        )
        return connection
    except Exception as e:
        return f"Error: {e}"

def home_view(request):
    connection = db_connect()
    if isinstance(connection, str):  # Check if it returned an error
        return Response(connection)

    # Proceed with your database operations
    return Response("Connection successful!")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(home_view, route_name='home')
        app = config.make_wsgi_app()
