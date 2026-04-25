
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='password',
            host='localhost',
            port='5432'
        )
        print("Connection successful")
        return conn
    except Exception as e:
        print(f"Connection error: {e}")

# Call the function
if __name__ == "__main__":
    connect_to_db()
