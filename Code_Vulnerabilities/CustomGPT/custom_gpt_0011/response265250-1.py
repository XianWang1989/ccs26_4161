
import os
import psycopg2
from wsgiref.simple_server import make_server

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='your_password',
            host='localhost',
            port='5432'
        )
        return "Connection successful!"
    except Exception as e:
        return f"Error connecting to database: {str(e)}"

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    return [connect_to_db().encode('utf-8')]

if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
