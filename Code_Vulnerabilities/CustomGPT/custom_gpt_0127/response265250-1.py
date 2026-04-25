
import psycopg2
from psycopg2 import sql

try:
    connection = psycopg2.connect(
        dbname='db_name',
        user='username',
        password='your_password',
        host='127.0.0.1',
        port='5432'
    )

    cursor = connection.cursor()
    cursor.execute(sql.SQL("SELECT version();"))
    version = cursor.fetchone()
    print(f"PostgreSQL version: {version}")

except Exception as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
