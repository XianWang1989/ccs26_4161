
import os
from wsgiref.simple_server import make_server
import postgresql

def application(environ, start_response):
    try:
        # Establish a connection to the database
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        # Your database operations go here
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'Connected to the database!']
    except postgresql.exceptions.ClientCannotConnectError as e:
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [str(e).encode()]

if __name__ == '__main__':
    with make_server('', 8000, application) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
