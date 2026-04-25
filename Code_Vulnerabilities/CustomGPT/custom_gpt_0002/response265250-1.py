
from pyramid.config import Configurator
from pyramid.response import Response
import psycopg2

def db_connect():
    try:
        conn = psycopg2.connect("dbname='db_name' user='username' host='localhost' password='password'")
        return conn
    except Exception as e:
        return str(e)

def hello_world(request):
    conn_response = db_connect()
    return Response(f"Connection Response: {conn_response}")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
