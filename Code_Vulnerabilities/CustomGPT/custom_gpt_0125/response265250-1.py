
import psycopg2
from psycopg2 import sql

try:
    # Establish the connection
    connection = psycopg2.connect(
        dbname='db_name',
        user='username',
        password='your_password',
        host='localhost',
        port='5432'
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute(sql.SQL("SELECT version();"))

    # Fetch and print the results
    db_version = cursor.fetchone()
    print(f"Database version: {db_version}")

except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")
finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()
