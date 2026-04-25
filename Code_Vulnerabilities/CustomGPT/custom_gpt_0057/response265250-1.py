
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)

try:
    conn = psycopg2.connect(
        dbname='db_name',
        user='username',
        password='your_password',
        host='localhost',
        port='5432'
    )
    logging.info("Connection successful!")
except Exception as e:
    logging.error("Connection failed: %s", e)
