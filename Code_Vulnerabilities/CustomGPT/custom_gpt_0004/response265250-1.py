
import psycopg2

try:
    connection = psycopg2.connect(
        dbname='db_name',
        user='username',
        password='password',
        host='127.0.0.1',
        port='5432'
    )
    print("Connection successful")
except Exception as e:
    print("Error connecting to the database:", e)
