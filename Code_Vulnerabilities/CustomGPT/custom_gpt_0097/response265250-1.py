
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
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()

        response_body = f"<p>PostgreSQL version: {db_version}</p>"
        cursor.close()
        conn.close()

        status = '200 OK'
    except Exception as e:
        response_body = f"<p>Error: {str(e)}</p>"
        status = '500 Internal Server Error'

    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    return [response_body.encode('utf-8')]

if __name__ == "__main__":
    server = make_server('localhost', 8000, application)
    print("Serving on port 8000...")
    server.serve_forever()
