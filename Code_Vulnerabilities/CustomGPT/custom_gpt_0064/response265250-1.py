
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='your_password',
            host='127.0.0.1',  # Use 127.0.0.1 instead of localhost
            port='5432'
        )
        cursor = connection.cursor()
        # Example query
        cursor.execute(sql.SQL("SELECT version();"))
        db_version = cursor.fetchone()
        print("Database version:", db_version)
    except Exception as e:
        print("Error connecting to the database:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    connect_to_db()
