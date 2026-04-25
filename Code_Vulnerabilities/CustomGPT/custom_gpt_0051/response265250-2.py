
import psycopg2

try:
    conn = psycopg2.connect("dbname=db_name user=username password=password host=localhost")
    print("Connection successful")
except Exception as e:
    print(f"Connection error: {e}")
