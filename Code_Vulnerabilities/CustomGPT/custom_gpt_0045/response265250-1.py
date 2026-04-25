
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='password',
            host='localhost',
            port='5432'
        )
        print("Connection successful")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
