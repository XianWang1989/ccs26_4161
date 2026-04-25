
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def db_connection():
    # Replace 'username', 'password', 'db_name' with your actual credentials
    conn = postgresql.open('pq://username:password@localhost:5432/db_name')
    return conn

def my_view(request):
    conn = db_connection()
    with conn.xact() as transaction:
        result = conn.execute("SELECT * FROM my_table")
        # Process the result here
    return Response(f'Result: {result}')

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_view(my_view, route_name='my_view')
    return config.make_wsgi_app()
