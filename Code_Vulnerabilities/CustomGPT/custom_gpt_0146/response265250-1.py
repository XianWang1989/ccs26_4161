
import psycopg2

connection = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    user="your_username",
    password="your_password",
    database="db_name"
)
