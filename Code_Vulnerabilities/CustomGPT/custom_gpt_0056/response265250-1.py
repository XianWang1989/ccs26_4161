
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        # Define your database connection parameters
        connection_params = {
            'dbname': 'db_name',
            'user': 'your_user',
            'password': 'your_password',
            'host': '127.0.0.1',  # change this to your server's IP if needed
            'port': '5432'
        }

        # Create a connection
        conn = psycopg2.connect(**connection_params)
        print("Connection successful")

        # Return the connection object
        return conn

    except psycopg2.Error as e:
        print(f"Unable to connect: {e}")
        return None

# Call the function to connect
db_connection = connect_to_db()
