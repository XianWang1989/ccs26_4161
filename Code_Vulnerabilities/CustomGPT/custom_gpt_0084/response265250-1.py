
import psycopg2
from psycopg2 import sql

def connect_db():
    try:
        connection = psycopg2.connect(
            dbname="db_name",
            user="username",
            password="secure_password",
            host="127.0.0.1",
            port="5432"
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Usage
if __name__ == "__main__":
    conn = connect_db()
    if conn:
        print("Database connection established.")
        conn.close()
