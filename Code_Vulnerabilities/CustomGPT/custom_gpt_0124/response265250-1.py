
import os
from wsgiref.simple_server import make_server
import psycopg2

def application(environ, start_response):
    try:
        conn = psycopg2.connect(
            dbname="db_name",
            user="username",
            password="password",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        response_body = f"Database version: {db_version[0]}".encode('utf-8')
        status = '200 OK'
    except Exception as e:
        response_body = str(e).encode('utf-8')
        status = '500 Internal Server Error'
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()

    headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]
    start_response(status, headers)
    return [response_body]

if __name__ == '__main__':
    server = make_server('127.0.0.1', 8051, application)
    print("Serving on port 8051...")
    server.serve_forever()
