
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

# Update with your database credentials
DB_USER = 'username'
DB_PASSWORD = 'your_password'
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'db_name'

def get_db_connection():
    try:
        db = postgresql.open(f'pq://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        print(f"Connection error: {e}")
        return None

def hello_world(request):
    db = get_db_connection()
    if db:
        return Response("Connected to the database!")
    return Response("Failed to connect to the database.")

if __name__ == '__main__':
    config = Configurator()
    config.add_route('home', '/')
    config.add_view(hello_world, route_name='home')
    app = config.make_wsgi_app()
