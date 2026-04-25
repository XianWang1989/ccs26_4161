
import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError

def create_connection():
    try:
        connection = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='password',
            host='127.0.0.1',
            port='5432'
        )
        print("Connection successful!")
        return connection
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# Usage
if __name__ == "__main__":
    conn = create_connection()
