
import psycopg2
from psycopg2 import sql

try:
    # Define the connection parameters
    conn = psycopg2.connect(
        dbname='db_name',
        user='username',
        password='password',
        host='localhost',
        port='5432'
    )
    print("Connection established!")

    # Create a cursor object
    cur = conn.cursor()

    # Execute a simple SQL query
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print(f"Database version: {db_version}")

    # Clean up
    cur.close()
    conn.close()

except psycopg2.OperationalError as e:
    print(f"Operational error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
