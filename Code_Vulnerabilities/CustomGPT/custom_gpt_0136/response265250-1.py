
import psycopg2
from pyramid.config import Configurator

def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname='db_name',
            user='username',
            password='password',
            host='localhost',
            port='5432'
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

if __name__ == "__main__":
    with Configurator() as config:
        config.scan()
