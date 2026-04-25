
import psycopg2
from psycopg2 import pool

# Database connection parameters
DATABASE_URL = "postgresql://username:password@localhost:5432/db_name"

try:
    # Create a connection pool
    connection_pool = psycopg2.pool.SimpleConnectionPool(1, 10, DATABASE_URL)

    # Get a connection from the pool
    connection = connection_pool.getconn()

    # Execute a simple query
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Connected to:", db_version)

    # Clean up
    cursor.close()
    connection_pool.putconn(connection)

except Exception as e:
    print("Error while connecting to PostgreSQL:", e)
