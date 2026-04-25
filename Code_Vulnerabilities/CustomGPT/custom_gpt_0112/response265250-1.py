
from pyramid.config import Configurator
from pyramid.response import Response
import postgresql

def db_connect():
    try:
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        print(f"Database connection error: {e}")

def my_view(request):
    db = db_connect()
    # Proceed with your logic using db connection
    return Response("Database connected successfully!")

if __name__ == '__main__':
    config = Configurator()
    config.add_route('my_view', '/')
    config.scan()
