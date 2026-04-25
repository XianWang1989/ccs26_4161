
import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        # Establishing the connection
        connection = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='your_password',
            host='127.0.0.1',
            port='5432'
        )
        cursor = connection.cursor()
        print("Connection established!")

        # Example query
        cursor.execute(sql.SQL("SELECT version();"))
        db_version = cursor.fetchone()
        print(f"PostgreSQL version: {db_version}")

    except Exception as error:
        print(f"Error occurred: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

connect_to_db()
