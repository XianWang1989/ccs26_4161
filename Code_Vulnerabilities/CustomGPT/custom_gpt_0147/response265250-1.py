
import postgresql
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def connect_to_db():
    try:
        # Replace the below values with your username, password, host, port, and database name
        db_url = 'pq://username:password@localhost:5432/db_name'

        # Connect to the PostgreSQL database
        db = postgresql.open(db_url)
        logging.info("Database connection successful.")

        # Perform any database operations here
        # ...

    except postgresql.exceptions.ClientCannotConnectError as e:
        logging.error("Client cannot connect to server: %s", e)
    except postgresql.exceptions.ConnectionRejectionError as e:
        logging.error("Connection rejected: %s", e)
    except Exception as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    connect_to_db()
