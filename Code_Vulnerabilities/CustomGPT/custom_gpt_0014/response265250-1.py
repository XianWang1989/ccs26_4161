
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.response import Response

def get_db_connection():
    # Example connection string
    connection_string = 'postgresql://username:password@localhost:5432/db_name'
    engine = engine_from_config({'sqlalchemy.url': connection_string}, prefix='sqlalchemy.')
    connection = engine.connect()
    return connection

def my_view(request):
    conn = get_db_connection()
    result = conn.execute("SELECT * FROM my_table")
    data = result.fetchall()
    conn.close()
    return Response(str(data))

if __name__ == "__main__":
    with Configurator() as config:
        config.add_route('my_view', '/')
        config.add_view(my_view, route_name='my_view')
        app = config.make_wsgi_app()
