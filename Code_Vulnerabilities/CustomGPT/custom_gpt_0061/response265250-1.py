
import psycopg2
from wsgiref.simple_server import make_server

def application(environ, start_response):
    conn = None
    try:
        # Update with your connection details
        conn = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='password',
            host='localhost',
            port='5432'
        )

        # Create a cursor and execute a query
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()

        response_body = f"PostgreSQL version: {version[0]}".encode('utf-8')
        status = '200 OK'

    except Exception as e:
        response_body = str(e).encode('utf-8')
        status = '500 Internal Server Error'

    finally:
        if conn:
            conn.close()

    headers = [('Content-Type', 'text/plain; charset=utf-8'),
               ('Content-Length', str(len(response_body)))]
    start_response(status, headers)
    return [response_body]

if __name__ == '__main__':
    server = make_server('localhost', 8000, application)
    print("Serving on port 8000...")
    server.serve_forever()
