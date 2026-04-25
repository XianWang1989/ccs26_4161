
import psycopg2
from psycopg2 import sql

def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='password',
            host='127.0.0.1',
            port='5432'
        )
        return connection
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

def fetch_data():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM your_table;")
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        return records

# Example usage
if __name__ == "__main__":
    data = fetch_data()
    print(data)
