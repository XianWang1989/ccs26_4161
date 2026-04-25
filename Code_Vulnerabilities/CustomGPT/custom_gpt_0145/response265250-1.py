
import psycopg2

try:
    # Replace username, password, db_name with your actual values
    connection = psycopg2.connect(
        user="username",
        password="your_password",
        host="127.0.0.1",
        port="5432",
        database="db_name"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"You are connected to - {db_version}")
except Exception as error:
    print(f"Error connecting to PostgreSQL database: {error}")
finally:
    if connection:
        cursor.close()
        connection.close()
