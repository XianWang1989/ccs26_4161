
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="db_name",
            user="username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

db_connection = connect_to_db()
if db_connection:
    print("Connection successful")
else:
    print("Connection failed")
