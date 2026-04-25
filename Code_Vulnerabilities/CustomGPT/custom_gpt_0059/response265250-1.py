
from pyramid.config import Configurator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pyramid.response import Response

def get_database_connection():
    # Replace the placeholders with your actual values
    username = 'your_username'
    password = 'your_password'
    host = 'localhost'
    port = '5432'
    database = 'your_db_name'

    connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)
    return sessionmaker(bind=engine)()

def my_view(request):
    session = get_database_connection()
    # Perform database operations
    return Response('Database connected successfully!')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_view(my_view, route_name='my_view')
        app = config.make_wsgi_app()
