
import psycopg2
from psycopg2 import sql, OperationalError

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            user="your_username",
            password="your_password",
            host="127.0.0.1",
            port="5432",
            database="your_database"
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Usage
conn = create_connection()
