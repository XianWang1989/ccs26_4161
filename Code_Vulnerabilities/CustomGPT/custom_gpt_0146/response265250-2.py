
import psycopg2
from psycopg2 import OperationalError

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            host="127.0.0.1",
            port=5432,
            user="your_username",
            password="your_password",
            database="db_name"
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Usage
if __name__ == "__main__":
    conn = create_connection()
