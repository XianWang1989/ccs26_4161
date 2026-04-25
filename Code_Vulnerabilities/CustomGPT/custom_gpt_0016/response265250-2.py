
import os
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        # Use environment variable for connection string or hardcode it
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME', 'db_name'), 
            user=os.getenv('DB_USER', 'username'), 
            password=os.getenv('DB_PASSWORD', 'password'), 
            host='localhost', 
            port='5432'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Connected to PostgreSQL database: {db_version}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    connect_to_db()
