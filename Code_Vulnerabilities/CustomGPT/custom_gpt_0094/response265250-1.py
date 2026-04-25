
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        # Connect to your postgres DB
        connection = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='your_password',
            host='127.0.0.1',
            port='5432'
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a query
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except Exception as e:
        print("Error connecting to database:", e)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection closed.")

# Call the function
connect_to_db()
