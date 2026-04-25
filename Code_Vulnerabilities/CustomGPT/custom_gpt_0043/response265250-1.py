
from pyramid.config import Configurator
from pyramid.response import Response
import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        dbname='db_name',
        user='username',
        password='your_password',
        host='localhost',
        port='5432'
    )
    return conn

def my_view(request):
    try:
        conn = connect_to_db()
        # Do something with the connection
        return Response('Connection established!')
    except Exception as e:
        return Response(f'Error: {str(e)}')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('my_view', '/')
        config.add_view(my_view, route_name='my_view')
        app = config.make_wsgi_app()
