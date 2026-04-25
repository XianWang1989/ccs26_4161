
import psycopg2
from pyramid.config import Configurator

def get_db_connection():
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
        print(f"Database connection error: {e}")
        raise

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_view('myapp.views.my_view', route_name='home')
    return config.make_wsgi_app()
