
import postgresql
from wsgiref.simple_server import make_server

def application(environ, start_response):
    try:
        # Connect to the PostgreSQL database
        db = postgresql.open("pq://username:password@localhost/db_name")
        response_body = "Connection to database successful!"
    except postgresql.exceptions.ConnectionError as e:
        response_body = f"Failed to connect to database: {str(e)}"

    status = '200 OK' if 'successful' in response_body else '500 Internal Server Error'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    return [response_body.encode('utf-8')]

if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    httpd.serve_forever()
