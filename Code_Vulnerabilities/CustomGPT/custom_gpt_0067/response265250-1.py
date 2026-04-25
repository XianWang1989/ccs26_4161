
# myapp.py
import os
import psycopg2
from wsgiref.simple_server import make_server

def application(environ, start_response):
    try:
        conn = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='password',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        version = cursor.fetchone()

        response_body = f"PostgreSQL version: {version[0]}"
        cursor.close()
        conn.close()
    except Exception as e:
        response_body = f"Error connecting to database: {e}"

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    return [response_body.encode('utf-8')]

if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
