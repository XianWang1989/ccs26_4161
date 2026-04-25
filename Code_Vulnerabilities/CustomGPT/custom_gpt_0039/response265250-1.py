
from pyramid.config import Configurator
from pyramid.response import Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_connection():
    # Adjust the connection string as necessary
    DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

def my_view(request):
    session = get_db_connection()
    # Use the session for database operations
    # ...
    return Response("Hello, Database!")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('my_view', '/')
        config.scan()
        app = config.make_wsgi_app()
