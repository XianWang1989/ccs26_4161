
import psycopg2

try:
    connection = psycopg2.connect(
        dbname='db_name',
        user='username',
        password='password',
        host='localhost',
        port='5432'
    )
    print("Connection successful")
except psycopg2.Error as e:
    print(f"Error: {e}")
finally:
    if connection:
        connection.close()
