
# simple_wsgi_app.py
import os
from postgresql import dbapi

def application(environ, start_response):
    try:
        conn = dbapi.connect('pq://username:password@localhost:5432/db_name')
        response_body = b"Database connection successful!"
        status = '200 OK'
    except Exception as e:
        response_body = f"Error: {str(e)}".encode('utf-8')
        status = '500 Internal Server Error'

    headers = [('Content-Type', 'text/plain'),
               ('Content-Length', str(len(response_body)))]
    start_response(status, headers)
    return [response_body]
