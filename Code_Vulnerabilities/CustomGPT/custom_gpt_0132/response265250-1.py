
from pyramid.config import Configurator
from pyramid.response import Response
import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='password',
            host='localhost',
            port='5432'
        )
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

def hello_world(request):
    conn = connect_to_db()
    if conn:
        return Response("Connected to the database!")
    else:
        return Response("Failed to connect to the database.")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
