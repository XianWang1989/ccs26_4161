
import psycopg2
from pyramid.config import Configurator
from pyramid.response import Response

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname='db_name',
            user='your_username',
            password='your_password',
            host='localhost',
            port='5432'
        )
        return connection
    except Exception as e:
        return Response(f"Error connecting to the database: {str(e)}", status=500)

def my_view(request):
    connection = get_connection()
    return Response("Successfully connected to the database!")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('my_view', '/')
        config.scan()
    app = config.make_wsgi_app()

