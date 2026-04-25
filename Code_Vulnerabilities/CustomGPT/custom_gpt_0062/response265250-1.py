
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

# Database connection settings
DB_USER = 'username'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'db_name'

def get_db_connection():
    conn_string = f'pq://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    return postgresql.open(conn_string)

def hello_world(request):
    db = get_db_connection()
    # Example query
    result = db.prepare("SELECT * FROM your_table")()
    return Response(f"Hello World! Data: {result}")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
