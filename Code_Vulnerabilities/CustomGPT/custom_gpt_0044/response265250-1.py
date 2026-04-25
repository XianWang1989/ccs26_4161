
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def connect_db():
    # Adjust connection string parameters as needed
    db = postgresql.open('pq://username:password@localhost:5432/db_name')
    return db

def my_view(request):
    db = connect_db()
    result = db.query("SELECT * FROM my_table")
    return Response(str(result))

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('my_view', '/')
    config.add_view(my_view, route_name='my_view')
    return config.make_wsgi_app()
