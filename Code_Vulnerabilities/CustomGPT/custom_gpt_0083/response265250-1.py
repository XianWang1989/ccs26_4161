
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        # Establish the connection
        conn = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='your_password',
            host='localhost',
            port=5432
        )
        print("Connection successful")
        return conn

    except psycopg2.OperationalError as e:
        print("Unable to connect to the database:", e)

# Call the function
if __name__ == "__main__":
    connection = connect_to_db()
