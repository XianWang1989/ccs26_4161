
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        # Adjust the connection string to use TCP/IP
        conn = psycopg2.connect("dbname='db_name' user='username' password='password' host='127.0.0.1' port='5432'")
        print("Connection successful")
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    connect_to_db()
