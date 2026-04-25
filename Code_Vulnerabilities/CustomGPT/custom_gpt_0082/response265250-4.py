
import os
import sys
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

# Activate your virtual environment
activate_this = '/path/to/your/virtualenv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

def connect_to_db():
    try:
        db = postgresql.open('pq://username:password@/db_name?host=/var/run/postgresql')
        return db
    except Exception as e:
        print(f"Database connection error: {e}")

def my_view(request):
    db = connect_to_db()
    if db:
        return Response("Connected to the database!")
    return Response("Failed to connect to the database.")

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('my_view', '/')
    config.add_view(my_view, route_name='my_view')
    return config.make_wsgi_app()
