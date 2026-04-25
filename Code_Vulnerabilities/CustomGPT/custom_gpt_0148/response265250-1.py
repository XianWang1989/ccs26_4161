
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        # Adjust connection parameters as needed
        connection = psycopg2.connect(
            dbname="db_name",
            user="username",
            password="your_password",
            host="127.0.0.1",  # Use 127.0.0.1 instead of localhost
            port="5432"
        )
        print("Connection successful")
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")

# Usage
if __name__ == "__main__":
    connect_to_db()
