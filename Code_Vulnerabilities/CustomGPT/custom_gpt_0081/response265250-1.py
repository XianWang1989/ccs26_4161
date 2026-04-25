
from pyramid.config import Configurator
from pyramid.response import Response
import psycopg2

def get_db_connection():
    try:
        # Change the connection parameters accordingly
        connection = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='your_password',
            host='localhost',
            port='5432'
        )
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

def hello_world(request):
    connection = get_db_connection()
    if connection:
        return Response("Connected to the database!")
    else:
        return Response("Failed to connect to the database.")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
